import requests
import os
from msal import PublicClientApplication
from dotenv import load_dotenv

load_dotenv()
TENANT_ID=os.getenv("TENANT_ID")
CLIENT_ID=os.getenv("CLIENT_ID")

def get_access_token():
    authority = f'https://login.microsoftonline.com/organizations'
    app = PublicClientApplication(CLIENT_ID, authority=authority)
    scopes = ['User.Read', 'Tasks.Read', 'Directory.Read.All']
    result = app.acquire_token_interactive(scopes=scopes)

    if "access_token" in result:
        return result["access_token"]
    else:
        print(result.get("error"))
        print(result.get("error_description"))
        return None 
