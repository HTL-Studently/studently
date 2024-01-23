import asyncio
import re
from app.db.schemas import Student
from app.db.dbhandler import DBHandler
from app.graph.graph import GraphAPI



class Logic():
    def __init__(self) -> None:
        # self.db = DBHandler()
        self.graph = GraphAPI()


    async def graph_get_all_users(self, access_token):
        # Get all users from GraphAPI

        next_link = "https://graph.microsoft.com/v1.0/users"
        all_student = []

        while next_link:
            response = await self.graph.get_request(access_token=access_token, full_url=next_link)  

            try:
                next_link = response["content"]["@odata.nextLink"]
            except KeyError:
                print("Reached End")
                next_link = False

            # Sort entries for actuall students
            for person in response["content"]["value"]:

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
                        type = "Student", #str(person["jobTitle"]),
                        sclass = str(sclass),
                        owned_objects = [],
                    )

                    all_student.append(student)

        return all_student



