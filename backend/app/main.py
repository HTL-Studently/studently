import os
from datetime import datetime, timedelta
from typing import Annotated, Union
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel
from dotenv import load_dotenv

from app.security import SecurityFunctions
from app.db.schemas import Student, Admin, Token
from app.db.dbhandler import DBHandler
from app.api import api_logic

#TODO

# Split API Endpoints into multiple files
# https://fastapi.tiangolo.com/tutorial/bigger-applications/


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

# Test Endpoint
@app.get("/test")
async def test_api():
    return "Pong"


# Login Endpoints

@app.post("/signup", tags=["login"], response_model=Student)
async def create_user(data: Student):
    # Query Database to check if user exists

    if not db.read_student("eamil", data.email):
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
        return user

    else:    
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User {data.email} already exists"
        )

@app.post('/login', tags=["login"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.read_admin("username", form_data.username)
    if not user:
        user = db.read_student("username", form_data.username)

    
    if user:
        # Skip Hash verification until password hashing is implimented in the frontend
        # hashed_pass = user['passwd']
        # if not sec.verify_hash(form_data.password, hashed_pass):
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST,
        #         detail="Incorrect email or password"
        #     )

        return {
            "access_token": sec.create_access_token(user['email']),
            "refresh_token": sec.create_refresh_token(user['email']),
        }


    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Incorrect email or password"
    )




# Student manipulation Endpoints

@app.post("/manstudent", tags=["sum"], response_model=Student)
async def create_student(data: Student):
    # Query Database to check if user exists

    if not db.read_student("eamil", data.email):
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
        return user

    else:    
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User {data.email} already exists"
        )


@app.get("/manstudent", tags=["sum"], response_model=Student)
async def get_student(data: Student):
    pass


@app.put("manstudent", tags=["sum"], response_model=Student)
async def update_student(data: Student):
    pass


@app.delete("/manstudent", tags=["sum"], response_model=Student)
async def delete_student(data: Student):
    pass


# Admin manipulation Endpoints

@app.post("/manadmin", tags=["aum"])
async def create_admin():
    pass

@app.get("/manadmin", tags=["aum"])
async def get_admin():
    pass

@app.put("/manadmin", tags=["aum"])
async def update_admin():
    pass

@app.delete("/manadmin", tags=["aum"])
async def delete_admin():
    pass


# User Information

@app.get("/me", tags=["User Info"])
async def get_me(user = Depends(sec.get_current_user)):
    return user
