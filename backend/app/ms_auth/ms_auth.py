import requests
import os
from msal import PublicClientApplication
from dotenv import load_dotenv

load_dotenv()
TENANT_ID=os.getenv("TENANT_ID")
CLIENT_ID=os.getenv("CLIENT_ID")
CLIENT_SECRET=os.getenv("CLIENT_SECRET")

username = "simcice@edu.htl-villach.at"
password = "D-9,vn%Ztg'#K>&\g#.&"

def get_access_token():

    scopes = 'https://graph.microsoft.com/Tasks.Read https://graph.microsoft.com/Tasks.Read.Shared'

    # let the user consent the access to their data
    # print the needed URL to copy it to the address line of your browser:
    consent_url = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize?client_id={CLIENT_ID}&response_type=code&scope={scopes}&prompt=consent'

    print(f'Use this Consent URL in the users browser once: \n\n{consent_url}')









    scope = ['https://graph.microsoft.com/.default']
    token_url = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token'

    data = {
        'grant_type': 'password',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'username': username,
        'password': password,
        'scope': ' '.join(scope)
    }

    # Get the access token using ROPC flow
    response = requests.post(token_url, data=data)

    print("\n\n\n\nRESPONSE: ")
    print(response)

    if response.status_code == 200:
        token = response.json()['access_token']
        print("\n\nTOKEN:")
        print(token)
        return token
