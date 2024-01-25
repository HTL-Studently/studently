from datetime import datetime, timedelta
import json
from pydantic import BaseModel
import uuid
from typing import Literal, Any
from decimal import Decimal

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

class SClass(BaseModel):
    name: str
    year: datetime = datetime.now().year
    students: list[Student]

class ClassHead(BaseModel):
    disabled: bool = True
    identifier: str
    username: str
    firstname: str
    lastname: str
    email: str
    expires: datetime = datetime.now() + timedelta(days=365)
    created: datetime = datetime.now()
    type: str = "admin"

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
            "type": self.type,
        }


class Payment(BaseModel):
    id: str = str(uuid.uuid4())
    name: str
    author: Student | str
    target: Student | SClass | list[Student|SClass] 
    product: Any = None
    cost: float
    start_date: datetime = datetime.now()
    due_date: datetime
    expires: datetime = datetime.now() + timedelta(days=365)

    # def return_dict(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "type": self.type,
    #         "tags": self.tags,
    #         "disabled": self.disabled,
    #         "name" : self.name,
    #         "author" : self.author,
    #         "product" : self.product,
    #         "cost" : self.cost,
    #         "due_date" : self.due_date,
    #         "lable" : self.lable,
    #         "expires" : self.expires,
    #         }

class Admin(BaseModel):
    disabled: bool = True
    identifier: str
    username: str
    firstname: str
    lastname: str
    email: str
    expires: datetime = datetime.now() + timedelta(days=365)
    created: datetime = datetime.now()
    type: str = "admin"

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
            "type": self.type,
        }

class License(BaseModel):
    disabled: bool = True
    identifier: str
    license_name: str 
    license_group: str
    description: str = ""
    cost: str = ""
    expires: datetime = datetime.now() + timedelta(days=365)
    created: datetime = datetime.now()

    def return_dict(self):
        return {
            "disabled": self.disabled,
            "identifier": self.identifier,
            "license_name": self.license_name,
            "license_group": self.license_group,
            "description": self.description,
            "cost": self.cost,
            "expires": self.expires,
            "created": self.created,
        }

class LicenseGroup(BaseModel):
    disabled: bool = True
    identifier: str
    license_name: str 
    description: str = ""
    cost: str = ""
    expires: datetime = datetime.now() + timedelta(days=365)
    created: datetime = datetime.now()
    licenses: list = []

    def return_dict(self):
        return {
            "disabled": self.disabled,
            "identifier": self.identifier,
            "license_name": self.license_name,
            "description": self.description,
            "cost": self.cost,
            "expires": self.expires,
            "created": self.created,
            "licenses": self.licenses,
        }


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class APIinit(BaseModel): 
    access_token: str
    only_students: bool = False 
    only_admins: bool = False

    def return_dict(self):
        return {
            "access_token": access_token,
        }
        
