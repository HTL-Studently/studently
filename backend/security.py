from argon2 import PasswordHasher
from typing import Annotated, Union, Any


class SecurityFunctions():
    def __init__(self) -> None:
        self.ph = PasswordHasher()

        self.ACCESS_TOKEN_EXPIRE_MINUTES = 30
        self.REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24
        self.ALGORITHM = "HS256"
        self.JWT_SECRET_KEY = "3b987065af9d206264dbddc039cddc58a81e6ef3be9ae0374ba3d2cf95340f87"
        self.JWT_REFRESH_SECRET_KEY = "3b987065af9d206264dbddc039cddc58a81e6ef3be9ae0374ba3d2cf95340f87"


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


    def create_access_token(self,subject: Union[str, Any], expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        
        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, self.JWT_SECRET_KEY, self.ALGORITHM)
        return encoded_jwt


    def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=self.REFRESH_TOKEN_EXPIRE_MINUTES)
        
        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, self.JWT_REFRESH_SECRET_KEY, self.ALGORITHM)
        return encoded_jwt