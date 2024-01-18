from datetime import datetime, timedelta
import json
from pydantic import BaseModel
from uuid import uuid4
from typing import Literal

class Student(BaseModel):
    disabled: bool = True
    identifier: str
    username: str
    firstname: str
    lastname: str
    email: str
    expires: datetime = datetime.now() + timedelta(days=365)
    created: datetime = datetime.now()
    sclass: str
    type: str = "student"
    owned_objects: list = []

    def return_dict(self):
        return {
            "disabled": self.disabled,
            "identifier": self.identifier,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
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

    def return_dict(self):
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


class BaseObject(BaseModel):
    id: str = uuid4()
    name: str
    type: Literal["base", "lic", "pay"]
    tags: list = []
    disabled: bool = False

    def return_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "tags": self.tags,
            "disabled": self.disabled,
            }

class Payment(BaseObject):
    name: str
    author: str
    product: None = None
    cost: float
    due_date: datetime
    lable: list[str] = []
    expires: datetime = datetime.now() + timedelta(days=365)

    def return_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "tags": self.tags,
            "disabled": self.disabled,
            "name" : self.name,
            "author" : self.author,
            "product" : self.product,
            "cost" : self.cost,
            "due_date" : self.due_date,
            "lable" : self.lable,
            "expires" : self.expires,
            }


class License(BaseObject):
    license_name: str
    cost: float = 0.0
    expires: datetime = datetime.now() + timedelta(days=365)
    license_data: dict = {}
    
    def return_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "tags": self.tags,
            "disabled": self.disabled,
            "license_name" : self.license_name,
            "cost" : self.cost,
            "expires" : self.expires,
            "license_data" : self.license_data,
            }



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None