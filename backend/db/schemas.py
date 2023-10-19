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
        }

# class ClassHead(Person):
#     manage_class: list = []

# class Admin(Person):
#     pass

class License():
    disabled: bool
    name: str
    cost: float = 0.0
    expires: datetime = datetime.now() + timedelta(days=365)
    license_data: dict = {}

class Payment():
    active: bool
    name: str
    author: str
    product: License|str
    cost: float
    due_date: datetime
    lable: list[str] = []
    expires: datetime = datetime.now() + timedelta(days=365)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None