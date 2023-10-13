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


# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

sec = SecurityFunctions()
db = dbhandler.DBHandler()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


@app.post("/signup", response_model=Student)
async def create_user(data: Student):
    # Query Database to check if user exists

    if not db.read_student("eamil", data.email):
        user = Student(
            disabled = data.disabled, 
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




@app.post('/login', response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.read_student("email", form_data.email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user['passwd']
    if not sec.verify_hash(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return {
        "access_token": sec.create_access_token(user['email']),
        "refresh_token": sec.create_refresh_token(user['email']),
    }



@app.get("/users")
async def get_users():
    pass