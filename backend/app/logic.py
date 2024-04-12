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
    Product, APIProduct
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

        access_token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IlFzWHgwbDlrbWtRS3B3Tld0VXRNVEUyWDkwMGY2NDRPVmF0d2tFRDRLWDQiLCJhbGciOiJSUzI1NiIsIng1dCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSIsImtpZCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzEyODE4NTg0LCJuYmYiOjE3MTI4MTg1ODQsImV4cCI6MTcxMjkwNTI4NCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhXQUFBQVZkMG9lVVp1NnhXT0MrbDNPcEFSUUw5M2gxcnhNN2tsWUd0bHBNRXN1TjVXYTdZNEV2WFpYQmp5SzNwcklsL1FvbytqcklxNHk1NVNQcE9UMW1xb1RJbXcyVTU2emttZkdFUGYxT0ZUWGhRPSIsImFtciI6WyJwd2QiLCJyc2EiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiNWFiMjE1MTUtZDE4Yy00ZGM2LTgwMjYtOWE1MzhiZGIzZjczIiwiZmFtaWx5X25hbWUiOiJLVU5PUyIsImdpdmVuX25hbWUiOiJQYW5uYSIsImlkdHlwIjoidXNlciIsImlwYWRkciI6Ijc4LjEwNC4xOTUuMTAiLCJuYW1lIjoiS1VOT1MgUGFubmEsIDVBSElUUyIsIm9pZCI6IjgyOGRjMTU4LTQ3NjUtNDRmMi05MDg4LTZlYWI2N2ZmYTJjNyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS03NzQ5MTYxMjEtNzg3MzI4ODA2LTkxMTgzMTAzNi0yMzg0MSIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMDZDMjk0MkQ1IiwicmgiOiIwLkFSQUEtbjRaS3h1T2dFYXlZNDRqZUltMXN3TUFBQUFBQUFBQXdBQUFBQUFBQUFDWEFPQS4iLCJzY3AiOiJEaXJlY3RvcnkuQWNjZXNzQXNVc2VyLkFsbCBEaXJlY3RvcnkuUmVhZC5BbGwgRGlyZWN0b3J5LlJlYWRXcml0ZS5BbGwgRWR1QXNzaWdubWVudHMuUmVhZFdyaXRlIEdyb3VwLlJlYWQuQWxsIEdyb3VwLlJlYWRXcml0ZS5BbGwgb3BlbmlkIHByb2ZpbGUgVXNlci5SZWFkIGVtYWlsIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiNnI3bHE0aU9nRnF2YjcwYW5ieFJmazBkU2luQUZhMy1md0FvVEhXVklWdyIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJFVSIsInRpZCI6IjJiMTk3ZWZhLThlMWItNDY4MC1iMjYzLThlMjM3ODg5YjViMyIsInVuaXF1ZV9uYW1lIjoia3Vub3NwQGVkdS5odGwtdmlsbGFjaC5hdCIsInVwbiI6Imt1bm9zcEBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1dGkiOiJPMmIzZFM5Y1ZVdW12Nktrc0ZXMEFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJ5T214eU1BZm05SnFabFdHQzg3Nm0wMkZ3T2xkaWxuZXE3SmhEbzNBdTVVIn0sInhtc190Y2R0IjoxMzU0MDEwMjY2LCJ4bXNfdGRiciI6IkVVIn0.Q_UephW6jkbGYtaxqoFlaIKSYo0D9vaqRdJ6eTLebZclsMTv3ta3-ggECokMsX5MjeyXmNfSBfN1JyxBQS0UXtc6TtHl5VsEdVaPLikkKGo_wrr1jvhuFeICQ5MdUBmsgSi4LLn3DPRFQuk8FWK-jrwbakaIsrtah27V2O1iSmmspzpbW7NsCl4uZOAYTi4sm_1cS0JOyOXX_uIleyVXA8b-J7JM_l6MviRw2D84tWmNWoD8RMyoW7S3HKDlTfvRWHMWARHOvM8f5u5MS6TxBLmIypC3TrtX7MnGhuBuaEdp5l5zXv5YmcoktkQdgU1R4Ec7voz8q8O5Qo82DUtSoA"

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

            # Sort entries for actual students      
            for person in response["content"]["value"]:

                # Search for students
                pattern = re.compile(r'^(?P<name>.*?),\s*(?P<class>\d\w+)$')

                match = pattern.match(person["displayName"])

                if match and not person["jobTitle"] == "Absolvent":
                    sclass = match.group('class')
                    all_sclass_raw.append(f"{sclass}-Schüler")

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

        all_sclass_raw = list(set(all_sclass_raw))
        all_sclass_raw = sorted(all_sclass_raw)
        all_sclass = []

        for sclass in all_sclass_raw:
            try:
                identifier = await self.graph.get_sclass_id(access_token=access_token, displayName=sclass)
                identifier = identifier["value"][0]["id"]   
                print(f"{sclass} - {identifier}")   
                all_sclass.append(SClass(name=sclass, identifier=identifier))
            except:
                print("Reached End")

        return {
            "all_students": all_students,
            "all_classHeads": all_classHeads,
            "all_sclass": all_sclass
        }



    async def assign_product(self, access_token: str, target_list: list, product_template: APIProduct): 

        # Translate targets to target-ids
        for target in target_list:
            id = await self.translate_name_to_id(access_token=access_token, target_name=target)
            student_list = []

            if id["type"] == "sclass":
                try:
                    sclass = target.replace("-Schüler", "")
                    student_list = self.db.read_student(search_par="sclass", search_val=sclass)

                except:
                    pass


            print(product_template)

            for student in student_list:
                student_product = Product(
                    disabled = product_template.disabled,
                    name = product_template.name,
                    author = product_template.author,
                    target = product_template.target,
                    info = product_template.info,
                    confirmation = "",
                    cost = product_template.cost,
                    iban = product_template.iban,
                    bic = product_template.bic,
                    start_date = product_template.start_date,
                    due_date = product_template.due_date,
                    expires = product_template.expires,
                    delete_date = product_template.delete_date,
                )

                response = self.db.assign_product(product=student_product, id=student["identifier"])
                print("RESPONSE: ", response)

    async def assign_license_to_msgroup(self, access_token: str, license_group: LicenseGroup):
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

    async def translate_name_to_id(self, access_token: str, target_name: str):
        """Tries to translate a name to a class or student id """

        # Try to find class in db
        response = self.db.read_sclass(search_par="name", search_val=target_name)
        if response["identifier"]:
            return {
                "id": response["identifier"],
                "type": "sclass"
                }
        else:
            raise ValueError("Failed to translate")