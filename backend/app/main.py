import os
from datetime import datetime, timedelta
from typing import Annotated, Optional, Union, Literal, Any
from fastapi import Depends, FastAPI, HTTPException, status, APIRouter, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel
from dotenv import load_dotenv
import json
from jose import jwt

from app.security import SecurityFunctions
from app.db.schemas import Student, Admin, Payment, BaseObject, Token, License
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

# Root Endpoint
@app.get("/", tags=["Test"])
async def root_api():
    return "Welcome to the Studently API"

# Test Endpoint
@app.get("/test", tags=["Test"])
async def test_api():
    return "Pong"


# Login Endpoints

@app.post("/signin", tags=["login"])
async def ms_signin(data: dict):

    access_token = data["accessToken"]
    id_token = data["idToken"]

    # Get Account from the access token
    account_data = await graph.get_user_account(access_token)

    # Get PFP from the access token
    account_pfp = graph.get_user_pfp(access_token)


    name_parts = account_data["displayName"].split(',')
    class_part = name_parts[-1].strip()

    new_student = Student(
        disabled = False, 
        identifier = id_token, 
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
        print("Student already exists - Updating")

        updated_fields = new_student.return_dict()

        for field, value in updated_fields.items():
            db.update_student(id=new_student.identifier, field=field, value=value)

        return {"message": {
            "profile": db_student,
            "pfp": account_pfp,
        }}
    
    # Add student
    else:
        print("Student did not exist")

        db_response = str(db.create_student(new_student))
        return {"message": db_response}


# Frontend Endpoint

@app.post("/profile")
async def get_profile(data: dict):

    access_token = data["accessToken"]

    db_student = db.read_student(search_par="identifier", search_val=data["idToken"])
    account_pfp = graph.get_user_pfp(access_token)

    return {"message": {
        "profile": db_student,
        "pfp": account_pfp,
    }}
    











# Student manipulation Endpoints

@app.post("/manstudent", tags=["User Management"], response_model=Student)
async def create_student(data: list[Student]):
    # Query Database to check if user exists

    for student in data:
        if not db.read_student(search_par="eamil", search_val=student.email):
            user = Student(
                disabled = True, 
                username = data.username,
                full_name = data.full_name,
                email = data.email,
                pwdhash = data.pwdhash,
                sclass = data.sclass,
                expires = datetime.now() + timedelta(days=365),
                created = datetime.now(),
            )

            # Add student to database
            db.create_student(user)
        
        else:    
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User {student.email} already exists"
            )
    
    return data

@app.get("/manstudent", tags=["User Management"], response_model=Student)
async def get_student(data: Student):
    pass

@app.put("manstudent", tags=["User Management"], response_model=Student)
async def update_student(data: Student):
    pass

@app.delete("/manstudent", tags=["User Management"], response_model=Student)
async def delete_student(data: Student):
    pass



# Admin manipulation Endpoints

@app.post("/manadmin", tags=["Admin Management"], response_model=Admin)
async def create_admin():
    pass

@app.get("/manadmin", tags=["Admin Management"], response_model=Admin)
async def get_admin():
    pass

@app.put("/manadmin", tags=["Admin Management"], response_model=Admin)
async def update_admin():
    pass

@app.delete("/manadmin", tags=["Admin Management"], response_model=Admin)
async def delete_admin():
    pass



# Student User Interface

@app.get("/me", tags=["Student User Interface"], response_model=Student)
async def get_me(user = Depends(sec.get_current_user)):
    return user



# Payments

@app.post("/obj", tags=["Student User Interface"], response_model=None)
async def create_payment(data: Payment, user = Depends(sec.get_current_user)):
    return db.add_payment(id = user.email, obj = data)

@app.get("/obj", tags=["Student User Interface"], response_model=None)
async def get_obj(user = Depends(sec.get_current_user)):
    return "Read Payment"

@app.put("/obj", tags=["Student User Interface"], response_model=None)
async def update_payment(user = Depends(sec.get_current_user)):
    return "Update Payment"

@app.delete("/obj", tags=["Student User Interface"], response_model=None)
async def delete_payment(data: Payment, user = Depends(sec.get_current_user)):
    return db.delete_payment(id = user.email, obj = data)



# Licenses

@app.post("/lic", tags=["Licenses"], response_model=None)
async def create_license(data: list[License], user = Depends(sec.get_current_user)):
    return db.create_license(licenses=data)

@app.get("/lic", tags=["Licenses"], response_model=None)
async def read_license(
    search_par: Optional[str] = Query("", description="Search parameter"), 
    search_val: Optional[str] = Query("", description="Search value")):
    return db.read_license(search_par=search_par, search_val=search_val)

@app.put("/lic", tags=["Licenses"], response_model=None)
async def update_payment(user = Depends(sec.get_current_user)):
    return "Update Payment"

# @app.delete("/lic", tags=["Licenses"], response_model=None)
# async def delete_payment(data: Payment, user = Depends(sec.get_current_user)):
#     return db.delete_payment(id = user.email, obj = data)