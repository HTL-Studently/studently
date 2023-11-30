from datetime import datetime, timedelta
from pydantic import BaseModel

class Student(BaseModel):
    disabled: bool
    username: str
    full_name: str
    email: str
    pwdhash: str|None = None
    expires: datetime = datetime.now() + timedelta(days=365)
    created: datetime = datetime.now()
    sclass: str
    type: str = "student"
    owned_objects: list

    def return_json(self):
        return {
            "disabled": self.disabled,
            "username": self.username,
            "full_name": self.full_name,
            "email": self.email,
            "pwdhash": self.pwdhash,
            "expires": self.expires,
            "created": self.created,
            "sclass": self.sclass,
            "type": self.type,
            "owned_objects": self.owned_objects,
        }

class Admin(BaseModel):
    disabled: bool
    username: str
    full_name: str
    email: str
    pwdhash: str|None = None
    expires: datetime = datetime.now() + timedelta(days=365)
    created: datetime = datetime.now()
    type: str = "admin"

    def return_json(self):
        return {
            "disabled": self.disabled,
            "username": self.username,
            "full_name": self.full_name,
            "email": self.email,
            "pwdhash": self.pwdhash,
            "expires": self.expires,
            "created": self.created,
            "type": self.type
        }

class StudentlyObject():
    id: str
    name: str
    tags: list
    archived: bool

class License(StudentlyObject):
    license_name: str
    disabled: bool
    cost: float = 0.0
    expires: datetime = datetime.now() + timedelta(days=365)
    license_data: dict = {}

class Payment(StudentlyObject):
    active: bool
    name: str
    author: str
    product: License|StudentlyObject|str
    cost: float
    due_date: datetime
    lable: list[str] = []
    expires: datetime = datetime.now() + timedelta(days=365)
    

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None