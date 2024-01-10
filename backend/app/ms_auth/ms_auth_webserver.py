import requests
import os
from msal import PublicClientApplication
from dotenv import load_dotenv
import http.server
import socketserver
import subprocess

PORT = 8000


class MyHandler(http.server.SimpleHTTPRequestHandler):


    load_dotenv()
    TENANT_ID=os.getenv("TENANT_ID")
    CLIENT_ID=os.getenv("CLIENT_ID")

    def do_GET(self):
        if self.path == '/run_script':
            self.run_script()
        else:
            super().do_GET()
        
    def get_access_token():

        print("HELLO")

        authority = f'https://login.microsoftonline.com/organizations'
        app = PublicClientApplication(CLIENT_ID, authority=authority)
        scopes = ['User.Read', 'Tasks.Read', 'Directory.Read.All']
        result = app.acquire_token_interactive(scopes=scopes)

        if "access_token" in result:
            print(access_token)
            return result["access_token"]
        else:
            print(result.get("error"))
            print(result.get("error_description"))
            return None 

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()













