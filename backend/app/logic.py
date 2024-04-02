import asyncio
import re
import uuid
from app.db.schemas import Student, Admin, LicenseGroup, ClassHead, Payment, SClass, License
from app.db.mongo import MongoDB
from app.graph.graph import GraphAPI


class Logic():
    def __init__(self) -> None:
        self.graph = GraphAPI()
        self.db = MongoDB()


    async def graph_get_all_students(self, access_token):

        # Gets all users in the class heads group (Replace group ID If necessary)
        next_link = "https://graph.microsoft.com/v1.0/groups/bab02613-a1c6-42d9-8e8f-db9180e828e3/members"
        all_classHeads = []
        while next_link:

            try:
                response = await self.graph.get_request(access_token=access_token, full_url=next_link)  
                next_link = response["content"]["@odata.nextLink"]
                print(".")

            except KeyError:
                print("Reached End")
                next_link = False
            except:
                next_link = False

            for person in response["content"]["value"]:
                class_head = ClassHead(
                    disabled = False,
                    identifier = str(person["id"]),
                    username = str(person["displayName"]),
                    firstname = str(person["givenName"]),
                    lastname = str(person["surname"]),
                    email = str(person["mail"]),
                    type = "ClassHead",
                )

                all_classHeads.append(class_head)


        # Gets all users in the student group (Replace group ID If necessary)
        next_link = "https://graph.microsoft.com/v1.0/groups/755bdf09-019e-41ed-b473-2fbd7931bf13/members"
        all_students = []
        all_sclass_raw = []
        while next_link:

            try:
                response = await self.graph.get_request(access_token=access_token, full_url=next_link)  
                next_link = response["content"]["@odata.nextLink"]

            except KeyError:
                print("Reached End")
                next_link = False
            except:
                next_link = False


            # Sort entries for actual students      
            for person in response["content"]["value"]:

                # Search for students
                pattern = re.compile(r'^(?P<name>.*?),\s*(?P<class>\d\w+)$')

                match = pattern.match(person["displayName"])

                if match and not person["jobTitle"] == "Absolvent":
                    sclass = match.group('class')
                    all_sclass_raw.append(sclass)

                    student = Student(
                        disabled = False,
                        identifier = str(person["id"]),
                        username = str(person["displayName"]),
                        firstname = str(person["givenName"]),
                        lastname = str(person["surname"]),
                        email = str(person["mail"]),
                        type = "Student",
                        sclass = str(sclass),
                        owned_objects = [],
                    )
                    all_students.append(student)

        # Filter and sort sclass list
            all_sclass_raw = list(set(all_sclass_raw))
            all_sclass_raw = sorted(all_sclass_raw)
            all_sclass = []

            for sclass in all_sclass_raw:
                all_sclass.append(SClass(name=sclass))

        return {
            "all_students": all_students,
            "all_classHeads": all_classHeads,
            "all_sclass": all_sclass
        }

    async def assign_payments(self, payment: Payment, target_type: str, target: str | list[str]):

        if target_type == "Student":

            if type(target) == list:
                for id in target:
                    self.db.update_student(id=id, field="owned_payments", value=payment, update_type="push")

            else:
                self.db.update_student(id=target, field="owned_payments", value=payment, update_type="push")
        
        elif target_type == "Class":
            pass

        else:
            pass

    async def assign_license_to_msgroup(self, access_token, license_group: LicenseGroup):
        """
        Used to design a license directly to a group or service identified by GraphAPI url 
        """



        # Try fetching with source as group
        path = f"groups/{license_group.source}/members"
        group_response = await self.graph.get_request(access_token=access_token, path=path)

        # Try fetching with source as service principle
        path = f"servicePrincipals/{license_group.source}/appRoleAssignedTo"
        service_principle_response = await self.graph.get_request(access_token=access_token, path=path)

        # Determin sucessful fetch
        if group_response["code"] == 200:
            successfull_response = group_response["content"]["value"]
            return
        
        elif service_principle_response["code"] == 200:
            successfull_response = service_principle_response["content"]["value"]
        
            # Assume entry is a class 
            for entry in successfull_response:
                
                # Get students by class
                path = f"/groups/{entry['principalId']}/members"
                students = await self.graph.get_request(access_token=access_token, path=path)

                students = students["content"]["value"]

                for student in students:
                    license = License(
                        disabled = False,
                        identifier = f"{license_group.identifier}#{str(uuid.uuid4())}",
                        license_name = license_group.license_name,
                        license_group = license_group.identifier,
                        description = license_group.description,
                        cost = license_group.cost,
                    )
                    license = license.__dict__

                    self.db.update_student(id=student["id"], update_type="push", field="owned_objects", value=license)

        
        else:
            print("Fetch failed - neither group or service")
            return

            

        # https://graph.microsoft.com/v1.0/servicePrincipals/680033ff-1040-43a8-a8db-18d8d6e81f9a/appRoleAssignedTo

