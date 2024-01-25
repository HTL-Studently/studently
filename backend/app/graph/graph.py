# GraphAPI helper file
import requests
import json



class GraphAPI:
    def __init__(self) -> None:
        self.base_url = "https://graph.microsoft.com/v1.0"

    

    def generate_headers(self, access_token):
        """Generates http headers
            - access_token = MS access token
        """

        headers = {
            'Authorization': f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
         
        return headers

    async def get_request(self, access_token: str, path: str = "", full_url: str = ""):
        """Send GET requests, returns request
            - headers = http headers
            - path = url path without base url (.../me)
            - full_url = entire url path (http://...)
        """

        headers = self.generate_headers(access_token)
        response = ""
        code = "0"
        url = ""

        if path:
            url = f"{self.base_url}/{path}"
        elif full_url:
            url = full_url

        try:
            response = requests.get(url=url , headers=headers)
            code = response.status_code

            # Decode response content
            response = json.loads(response.content.decode('utf-8'))

        except Exception as e:
            print(f"Error when fetching {url}\nError: {e}")





            
        return {"content": response, "code": code}

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
            return response.content

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def get_user_lic(self, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.get(f"{self.base_url}/me/licenseDetails", headers=headers)
            return response.content

        except Exception as e:
            print(f"An error occurred: {str(e)}")