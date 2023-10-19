import os
from datetime import datetime, timedelta
from typing import Annotated, Union
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from dotenv import load_dotenv

from security import SecurityFunctions
from db.schemas import Student, Token
from db import dbhandler

#TODO

# Split API Endpoints into multiple files
# https://fastapi.tiangolo.com/tutorial/bigger-applications/


# API Variables

load_dotenv()
CONTACT_NAME = os.environ.get("CONTACT_NAME")
CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL")

sec = SecurityFunctions()
db = dbhandler.DBHandler()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
description = ""

with open("./README.md") as file:
    description = file.read()

tags_metadata = [
    {
        "name": "login",
        "description": "Login and Signup",
    },
    {
        "name": "sum",
        "description": "Student User CRUD operations",
    },
    {
        "name": "aum",
        "description": "Admin User CRUD operations",
    },
    {
        "name": "suu",
        "description": "Student User Manipulation",
    }
]

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
    user = db.read_student("username", form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

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


# Studen User Endpoints

@app.get("/me", tags=["suu"])
async def get_me(user = Depends(sec.get_current_user)):
    # Authentification Check Example
    if isinstance(user, Student):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"User {user.email} is not authorized for this endpoint"
        )
    return user
