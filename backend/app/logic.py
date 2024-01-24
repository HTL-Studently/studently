import asyncio
import re
from app.db.schemas import Student, Admin, LicenseGroup
from app.db.dbhandler import DBHandler
from app.graph.graph import GraphAPI



class Logic():
    def __init__(self) -> None:
        # self.db = DBHandler()
        self.graph = GraphAPI()


    async def graph_get_all_students(self, access_token):
        # Get all users from GraphAPI

        # Get all classes 
        




        # Gets all users in the student group (Replace group ID If necessary)
        next_link = "https://graph.microsoft.com/v1.0/groups/755bdf09-019e-41ed-b473-2fbd7931bf13/members"
        all_students = []
        all_admins = []


        while next_link:

            try:
                response = await self.graph.get_request                (access_token=access_token, full_url=next_link)  
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
                    name = match.group('name').strip()
                    sclass = match.group('class')

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

        return {
            "all_students": all_students,
        }


    async def fill_license_group(self):
        pass

    
    async def attach_license(self):
        pass

    
    async def revoke_license(self):
        pass
