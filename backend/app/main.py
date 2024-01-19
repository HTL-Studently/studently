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

from app.security import SecurityFunctions
from app.db.schemas import Student, Payment, Token, License
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

db = DBHandler(
    STARTUP_ADMIN_USER = STARTUP_ADMIN_USER,
    STARTUP_ADMIN_PASSWD = STARTUP_ADMIN_PASSWD,
    STARTUP_ADMIN_EMAIL= STARTUP_ADMIN_EMAIL,
    )

sec = SecurityFunctions(
    dbhandler=db
)

graph = GraphAPI()

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

# Login Endpoints
@app.post("/signin", tags=["login"])
async def ms_signin(data: dict):

    access_token = data["accessToken"]
    id_token = data["idToken"]

    # Get Account from the access token
    account_data = await graph.get_user_account(access_token)

    print(f"\n\n\nACC: {account_data} \n\n\n")

    # Get PFP from the access token
    account_pfp = graph.get_user_pfp(access_token)


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
        owned_objects  = [])
    
    # Check if user already exists
    db_student = db.read_student(search_par="identifier", search_val=new_student.identifier)

    # If entry already exists, update it
    if db_student:
        updated_fields = new_student.return_dict()

        for field, value in updated_fields.items():
            if field in ["email, sclass, expires, firstname, lastname"]:
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

    print(f"\n\n\n\nDATA: {data}\n\n\n\n")


    db_student = db.read_student(search_par="identifier", search_val="96ec350d-ea90-406b-a6c6-94463948c77d")
    account_pfp = graph.get_user_pfp(access_token)

    response = {"message": {
        "profile": db_student,
        "pfp": account_pfp,
    }}

    return db_student



@app.post("/payment")
async def create_payment(data: Payment):

    new_payment = Payment(
        id = data.id,
        name = data.name,
        author = data.author,
        target = data.target,
        product = data.product,
        cost = data.cost,
        start_date = data.start_date,
        due_date = data.due_date,
        expires = data.expires,
    )

    db_response = str(db.create_payment(new_payment))

    return {"message": db_response}


@app.put("/payments")
async def update_payment(data: dict):
    id = data["id"]
    field = data["data"]
    value = data["value"]

    db_response = str(db.update_payment(id=id, field=field, value=value))
    

@app.get("/payments")
async def get_payments(data: dict):
    access_token = data["accessToken"]

    account = get_profile(data)["profile"]
    
    db_response = db.get_payment(id=data["id"], field=data["field"], value=data["value"])

    return {"message": {
        "payment": db_response
    }}




@app.get("licenses")
async def get_licenses(data: dict):
    pass

