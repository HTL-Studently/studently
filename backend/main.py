from datetime import datetime, timedelta
from typing import Annotated, Union
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from security import SecurityFunctions
from db.schemas import Student, Token
from db import dbhandler


sec = SecurityFunctions()
db = dbhandler.DBHandler()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


@app.post("/signup", response_model=Student)
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


@app.post('/login')
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


@app.get("/me")
async def get_me(user = Depends(sec.get_current_user)):
    return user


@app.post("/createStudent", response_model=Student)
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


@app.get("/getStudent", response_model=Student)
async def get_student(data: Student):
    pass


@app.get("updateStudent", response_model=Student)
async def update_student(data: Student):
    pass


@app.delete("/deleteStudent", response_model=Student)
async def delete_student(data: Student):
    pass