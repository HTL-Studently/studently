import os
from datetime import datetime, timedelta
from typing import Annotated, Optional, Union, Literal, Any
from fastapi import Depends, FastAPI, HTTPException, status, APIRouter, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel
from dotenv import load_dotenv
import json
from jose import jwt

# from app.security import SecurityFunctions
from app.db.schemas import Student, Payment, Token, License, APIinit, LicenseGroup
from app.logic import Logic
from app.db.dbhandler import DBHandler
from app.graph.graph import GraphAPI
from app.api import api_logic


#TODO

# Split API Endpoints into multiple files
# https://fastapi.tiangolo.com/tutorial/bigger-applications/



print("Welcome to Studently")

# API Variables

load_dotenv()
CONTACT_NAME = str(os.environ.get("CONTACT_NAME"))
CONTACT_EMAIL = str(os.environ.get("CONTACT_EMAIL"))
STARTUP_ADMIN_USER = str(os.environ.get("STARTUP_ADMIN_USER"))
STARTUP_ADMIN_PASSWD = str(os.environ.get("STARTUP_ADMIN_PASSWD"))
STARTUP_ADMIN_EMAIL = str(os.environ.get ("STARTUP_ADMIN_EMAIL"))


graph = GraphAPI()
db = DBHandler()
logic = Logic()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
description = ""

with open("./README.md") as file:
    description = file.read()

tags_metadata = api_logic.tags_metadata

# API

app = FastAPI(
    openapi_tags=tags_metadata,
    redoc_url=None,
    title="StudentlyAPI",
    description=description,
    summary="Studently Backend API",
    version="0.0.1",
    contact={
        "name": CONTACT_NAME,
        "emial": CONTACT_EMAIL,
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




######### Test Endpoints #########

@app.get("/", tags=["Test"])
async def root_api():
    return "Welcome to the Studently API"

# Test Endpoint
@app.get("/test", tags=["Test"])
async def test_api():
    return "Pong"



######### Login Endpoints #########


# Initiate Database
@app.post("/initdb", tags=["initdb"])
async def initialize_db(data: APIinit):
    access_token = data.access_token

    users = await logic.graph_get_all_students(access_token)
    all_students = users["all_students"]
    all_classHeads = users["all_classHeads"]

    db.create_student(all_students)
    db.create_classHead(all_classHeads)

    return {"message": {
        "all_students": all_students,
        "all_classHeads": all_classHeads,
    }}


# Get a (sorted) list of students
@app.get("/students", tags=["initdb"])
async def getStudentList(sclass: str = ""):
    
    if sclass:
        all_students = db.read_student(search_par="sclass", search_val=sclass)
        return all_students

    all_students = db.read_student()
    return {"message": all_students}





# Create a license group
@app.post("/licgroup", tags=["Licenses"])
async def create_license_group(lic_group: LicenseGroup):
    new_group = LicenseGroup(
        identifier = lic_group.identifier,
        license_name = lic_group.license_name,
        description = lic_group.description,
        cost = lic_group.cost,
        expires = lic_group.expires,
        licenses = lic_group.licenses,
    )

    created = db.create_license_group(licenses_group=new_group)


@app.post("/license", tags=["Licenses"])
async def create_license(license: License):
    new_license = License(
        disabled = license.disabled,
        identifier = license.identifier,
        license_name = license.license_name,
        license_group = license.license_group,
        description = license.description,
        cost = license.cost,
        expires = license.expires,
        created = license.created,
    )

    created = db.create_license([new_license])



# Login Endpoints
@app.post("/signin", tags=["login"])
async def ms_signin(data: dict):

    access_token = data["accessToken"]
    id_token = data["idToken"]

    # Get Account from the access token
    account_data = await graph.get_user_account(access_token)

    # Get PFP from the access token
    account_pfp = graph.get_user_pfp(access_token)

    # Get license data from the access token
    account_lic = graph.get_user_lic(access_token) 
    account_lic_str = account_lic.decode("utf-8")
    account_lic_dict = json.loads(account_lic_str)
    account_lic = account_lic_dict["value"][1]["servicePlans"]

    name_parts = account_data["displayName"].split(',')
    class_part = name_parts[-1].strip()

    new_student = Student(
        disabled = False, 
        identifier = account_data["id"], 
        username = account_data["displayName"], 
        firstname = account_data["givenName"],
        lastname = account_data["surname"], 
        email = account_data["mail"], 
        expires = datetime.now() + timedelta(days=365), 
        created = datetime.now(), 
        sclass = class_part, 
        type = "Student", 
        owned_objects  = account_lic)
    
    print("NEW: ", new_student)
    
    # Check if user already exists
    db_student = db.read_student(search_par="identifier", search_val=new_student.identifier)

    # If entry already exists, update it
    if db_student:
        updated_fields = new_student.return_dict()

        for field, value in updated_fields.items():
            if field in ["email, sclass, expires, firstname, lastname, owned_objects"]:
                db.update_student(id=new_student.identifier, field=field, value=value)

        return {"message": {
            "profile": db_student,
            "pfp": account_pfp,
        }}
    
    # Add student
    else:
        db_response = str(db.create_student(new_student))
        return {"message": db_response}







######### Frontend Endpoints #########

@app.post("/profile")
async def get_profile(data: dict):
    access_token = data["accessToken"]

    db_student = db.read_student(search_par="identifier", search_val="96ec350d-ea90-406b-a6c6-94463948c77d")
    account_pfp = graph.get_user_pfp(access_token)

    response = {"message": {
        "profile": db_student,
        "pfp": account_pfp,
    }}

    return db_student

