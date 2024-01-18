# GraphAPI helper file
import requests
from azure.identity import DeviceCodeCredential
from msgraph import GraphServiceClient

class GraphAPI:
    def __init__(self) -> None:
        self.base_url = "https://graph.microsoft.com/v1.0"


    async def get_user_account(self, access_token):
        headers = {
            'Authorization': f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.get(f"{self.base_url}/me", headers=headers)

            user_profile = response.json()
            return user_profile

        except Exception as e:
            print(f"An error occurred: {str(e)}")
    

    def get_user_pfp(self, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.get(f"{self.base_url}/me", headers=headers)
            print("R: ", response.content)
            return response.content

        except Exception as e:
            print(f"An error occurred: {str(e)}")