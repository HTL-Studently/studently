from argon2 import PasswordHasher
from typing import Union, Any
from datetime import datetime, timedelta
from jose import jwt
from typing import Union, Any
from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from db.dbhandler import DBHandler
from db.schemas import Student


reuseable_oauth = OAuth2PasswordBearer(tokenUrl="/login", scheme_name="JWT")


class SecurityFunctions():
    def __init__(self) -> None:
        self.ph = PasswordHasher()
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 30
        self.REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24
        self.ALGORITHM = "HS256"
        self.JWT_SECRET_KEY = "3b987065af9d206264dbddc039cddc58a81e6ef3be9ae0374ba3d2cf95340f87"
        self.JWT_REFRESH_SECRET_KEY = "3b987065af9d206264dbddc039cddc58a81e6ef3be9ae0374ba3d2cf95340f87"
        self.db = DBHandler()


    def hash_str(self, plain: str):
        """Returnes the hash of a string"""
        hashed_string = self.ph.hash(plain)
        if self.ph.verify(hashed_string, plain):
            return hashed_string


    def verify_hash(self, hashed_string: str, plain):
        """Verifies hash"""
        self.ph.verify(hashed_string, plain)


    def check_rehash(self, plain):
        """Rehashes password if needed"""
        if self.ph.check_needs_rehash:
            return self.hash_str(plain)


    def create_access_token(self,subject: Union[str, Any]) -> str:
        expires_delta = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        
        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, self.JWT_SECRET_KEY, self.ALGORITHM)
        return encoded_jwt


    def create_refresh_token(self, subject: Union[str, Any]) -> str:
        expires_delta = datetime.utcnow() + timedelta(minutes=self.REFRESH_TOKEN_EXPIRE_MINUTES)
        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, self.JWT_REFRESH_SECRET_KEY, self.ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(self, token: str = Depends(reuseable_oauth)) -> Student:
        try:
            payload = jwt.decode(
                token, self.JWT_SECRET_KEY, algorithms=["HS256"]
            )
            print(payload)

            if datetime.fromtimestamp(payload["exp"]) < datetime.now():
                raise HTTPException(
                    status_code = status.HTTP_401_UNAUTHORIZED,
                    detail="Token expired",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        except(jwt.JWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        student = self.db.read_student("email", payload["sub"])
        
        
        if student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Could not find user",
            )
        
        return Student(**student)