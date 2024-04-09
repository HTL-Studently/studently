import asyncio
import re
import uuid
from app.db.schemas import Student, Admin, LicenseGroup, ClassHead, Payment, SClass, License
from app.db.mongo import MongoDB
from app.graph.graph import GraphAPI
from app.db.schemas import (
    Student,
    Payment,
    License,
    APIinit,
    LicenseGroup,
    API,
    APIDefault,
    APIPayment,
    PaymentConfirmation,
    APIStudent,
    APIPaymentUpdate,
)

class Logic():
    def __init__(self) -> None:
        self.graph = GraphAPI()
        self.db = MongoDB()
        self.graph = GraphAPI()



    async def get_dbuser(self, graph_user, access_token: str):
        # try:
        id = graph_user["id"]

        db_student = self.db.read_student(search_par="identifier", search_val=id)

        if not db_student:
            data = APIinit(access_token=access_token)
            await initialize_db(
                data
            )  # Replace with faster function that only handles individual user
            db_student = self.db.read_student(search_par="identifier", search_val=id)

        if type(db_student) == list:
            db_student = db_student[0]

        if db_student:

            # Makes sure that these fields are lists
            # Quick fix, could be better
            if type(db_student["owned_objects"]) == str:
                db_student["owned_objects"] = []
            if type(db_student["owned_payments"]) == str:
                db_student["owned_payments"] = []

            user = Student(
                disabled=db_student["disabled"],
                identifier=db_student["identifier"],
                username=db_student["username"],
                firstname=db_student["firstname"],
                lastname=db_student["lastname"],
                email=db_student["email"],
                expires=db_student["expires"],
                created=db_student["created"],
                sclass=db_student["sclass"],
                type=db_student["type"],
                owned_objects=db_student["owned_objects"],
                owned_payments=db_student["owned_payments"],
            )

            return user
        else:
            return False

        # except Exception  as e:
        #     print(f"Authentication user failed: \n {e}")
        #     return False


    async def authorize_user(self, request):
        try:
            authorization_header = request.headers.get("authorization")
            if authorization_header:
                access_token = authorization_header[len("Bearer "):]
            else:
                access_token = request.cookies.get("accessToken")

            print(request.headers)

            if access_token is None:
                return {"error": "Authorization header is missing"}
            
            graph_user = await self.graph.get_user_account(access_token=access_token)
            user = await self.get_dbuser(graph_user=graph_user, access_token=access_token)


            return {"success": {
                "access_token": access_token,
                "user": user
                }
            }
    
        except Exception as error:
            return {"error": error}


    async def initialize_db(self, access_token):
        adobe_license = LicenseGroup(
            disabled = False,
            identifier = "adobeDefaultLicense",
            license_name = "AdobeLicense",
            description = "Adobe Default License",
            cost = "5€",
            source = "680033ff-1040-43a8-a8db-18d8d6e81f9a",
        )

        defaultLicense = [adobe_license]


        # Get students and teachers from GraphAPI
        users = await self.graph_get_all_students(access_token)
        all_students = users["all_students"]
        all_sclass = users["all_sclass"]
        all_classHeads = users["all_classHeads"]

        #  Write students and teachers to database
        self.db.create_student(all_students)
        self.db.create_classHead(all_classHeads)
        self.db.create_sclass(all_sclass)

        # Assign default licenses
        for group in defaultLicense:
            await self.assign_license_to_msgroup(access_token=access_token, license_group=group)

        return {
            "message": {
                "all_students": all_students,
                "all_classHeads": all_classHeads,
                "all_sclass": all_sclass,
            }
        }




    async def graph_get_all_students(self, access_token):

        # Gets all users in the class heads group (Replace group ID If necessary)
        next_link = "https://graph.microsoft.com/v1.0/groups/bab02613-a1c6-42d9-8e8f-db9180e828e3/members"
        all_classHeads = []

        access_token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6InFFaGhKVjVBel9wRG1IR0VQNldhT1VVSDB5OC1neWpoMHpaVEV2NzFRUDAiLCJhbGciOiJSUzI1NiIsIng1dCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSIsImtpZCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzEyNjk1MDc0LCJuYmYiOjE3MTI2OTUwNzQsImV4cCI6MTcxMjc4MTc3NSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhXQUFBQWJKSU9HM3I1ZEpPbjJ3T3V2UGF2ZVNBNG9uRTVCOWxKN2l0Um5hZWpKdEJ2K0hLMzZkaU9idk54L2tEYVFkSkpobk1OdS9pbG4wZ2VUalIwRzZkdUpiTENSVGtQUGlveEl2bTdPVmsrZUpRPSIsImFtciI6WyJwd2QiLCJyc2EiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiNWFiMjE1MTUtZDE4Yy00ZGM2LTgwMjYtOWE1MzhiZGIzZjczIiwiZmFtaWx5X25hbWUiOiJLVU5PUyIsImdpdmVuX25hbWUiOiJQYW5uYSIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjIxMy4xNjIuODEuMTYzIiwibmFtZSI6IktVTk9TIFBhbm5hLCA1QUhJVFMiLCJvaWQiOiI4MjhkYzE1OC00NzY1LTQ0ZjItOTA4OC02ZWFiNjdmZmEyYzciLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtNzc0OTE2MTIxLTc4NzMyODgwNi05MTE4MzEwMzYtMjM4NDEiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDA2QzI5NDJENSIsInJoIjoiMC5BUkFBLW40Wkt4dU9nRWF5WTQ0amVJbTFzd01BQUFBQUFBQUF3QUFBQUFBQUFBQ1hBT0EuIiwic2NwIjoiRGlyZWN0b3J5LkFjY2Vzc0FzVXNlci5BbGwgRGlyZWN0b3J5LlJlYWQuQWxsIERpcmVjdG9yeS5SZWFkV3JpdGUuQWxsIEVkdUFzc2lnbm1lbnRzLlJlYWRXcml0ZSBHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IjZyN2xxNGlPZ0ZxdmI3MGFuYnhSZmswZFNpbkFGYTMtZndBb1RIV1ZJVnciLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiRVUiLCJ0aWQiOiIyYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMiLCJ1bmlxdWVfbmFtZSI6Imt1bm9zcEBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1cG4iOiJrdW5vc3BAZWR1Lmh0bC12aWxsYWNoLmF0IiwidXRpIjoidjQtLUktX1ZfVUsyc0FxUzVDNXdBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYyI6WyJDUDEiXSwieG1zX3NzbSI6IjEiLCJ4bXNfc3QiOnsic3ViIjoieU9teHlNQWZtOUpxWmxXR0M4NzZtMDJGd09sZGlsbmVxN0poRG8zQXU1VSJ9LCJ4bXNfdGNkdCI6MTM1NDAxMDI2NiwieG1zX3RkYnIiOiJFVSJ9.0D6C8TFYqUmvNe4NdaOukBDpt_VitG1Q9JhUUI--w6vxsLrYl9Jcr7jHcBgKDimBryMD18DIgKyX3FNvdi6m1zbzJNiVpFLvd1XymgKSeiZPgcmaR789ZySFVxOVUd1KwA-9NLjaBnvIo438YUGbdhBjQnuq7tkJKEKvOmxlJPv8wB6KTUm1-hS876Z41Bd8cfGEXH1K3JmUgDwHQ3PlCfKtkfDa-26rp7VA2suJ2yRAgYa6LvVB10LZ_eC6yqJlpduv62zWlPu_na95zkHAvwI5floQ0Sqv-NqZyDh3V1rttIYFTpN0Sd_sc9Gfatb3WCLs53FV56ymF7e-r2-PDw"

        while next_link:
            try:
                response = await self.graph.get_request(access_token=access_token, full_url=next_link)  
                next_link = response["content"]["@odata.nextLink"]

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

