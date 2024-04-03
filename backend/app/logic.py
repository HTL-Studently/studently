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


        access_token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6Ijd2MVZ6WERMNnBZSXRxNWkxb0VrUDlKWGU0U3RGR1dKdUpvZkxWUkNUNzQiLCJhbGciOiJSUzI1NiIsIng1dCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSIsImtpZCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzEyMTM1NzE1LCJuYmYiOjE3MTIxMzU3MTUsImV4cCI6MTcxMjIyMjQxNSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhXQUFBQUpCemRqYkFlT1lHY0ZEVkZNc09Hdm1tbzlWKzArYTlFeWVVZVRyMEpSNGtlTEFad1BTN3YzUm9Sc3VyUk5JTXoiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IlNJTcSGScSGIiwiZ2l2ZW5fbmFtZSI6IkVyaWsiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyNjA2OjQwOjJjYjpjZTM1OjoxMjZhOjljZDEiLCJuYW1lIjoiU0lNxIZJxIYgRXJpaywgNUFISVRTIiwib2lkIjoiOTZlYzM1MGQtZWE5MC00MDZiLWE2YzYtOTQ0NjM5NDhjNzdkIiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTc3NDkxNjEyMS03ODczMjg4MDYtOTExODMxMDM2LTIzOTQxIiwicGxhdGYiOiIzIiwicHVpZCI6IjEwMDMyMDAwNkMyOTQzMEUiLCJyaCI6IjAuQVJBQS1uNFpLeHVPZ0VheVk0NGplSW0xc3dNQUFBQUFBQUFBd0FBQUFBQUFBQUNYQUZNLiIsInNjcCI6IkRpcmVjdG9yeS5BY2Nlc3NBc1VzZXIuQWxsIERpcmVjdG9yeS5SZWFkLkFsbCBEaXJlY3RvcnkuUmVhZFdyaXRlLkFsbCBFZHVBc3NpZ25tZW50cy5SZWFkV3JpdGUgR3JvdXAuUmVhZC5BbGwgR3JvdXAuUmVhZFdyaXRlLkFsbCBvcGVuaWQgcHJvZmlsZSBVc2VyLlJlYWQgZW1haWwiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiItcHlTSUpwYTZxR0VXanNKTm1NUFVPbnR4VnZKRk94T1hid19NVC1NLVZBIiwidGVuYW50X3JlZ2lvbl9zY29wZSI6IkVVIiwidGlkIjoiMmIxOTdlZmEtOGUxYi00NjgwLWIyNjMtOGUyMzc4ODliNWIzIiwidW5pcXVlX25hbWUiOiJzaW1jaWNlQGVkdS5odGwtdmlsbGFjaC5hdCIsInVwbiI6InNpbWNpY2VAZWR1Lmh0bC12aWxsYWNoLmF0IiwidXRpIjoiYzhyUDlOYTBxa2FaemRTQWNaRkRBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYyI6WyJDUDEiXSwieG1zX3NzbSI6IjEiLCJ4bXNfc3QiOnsic3ViIjoiblJrS1VNLWdabWtRYXF2M2xtSFR3dTNFajAxaG54UlNhOHFFY2FTcEhJdyJ9LCJ4bXNfdGNkdCI6MTM1NDAxMDI2NiwieG1zX3RkYnIiOiJFVSJ9.b_gvTwprTV8k84HMT0ltT0UfWHC7JOVXhc9zxuEfPn08JUKwiv6Zw-qTN8SXMOzIjUMN-Gihw5Rg2PxtBelspkhoQQtiZX3KAAOlIAjFeF1sxsuLiwbRyqAwUVFkp9sM3F4Adnsm3sSmH-Sp1rE27tnI7NKKiIAvWe60rtvNNy_9JQ6PaNF0tUSgo9X_9eSMx3WzjBkkRRw35_ir28zjsaF1tjHmW_InGLgGI9rj-f63_oC9jG3IdavDn3jFydecq1M-L30S2DgCyeWYHUBpUKJo4s3i13IFR4bTSYfA1MmM0D-KiKn74VWHNrsr2k5ZSky6jNA6A8q-UhlxYd07RA"




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


            print(response["content"])


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


            print(response)


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

