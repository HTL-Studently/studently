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
    owned_payments: list = []

    def return_dict(self):
        return {
            "disabled": str(self.disabled),
            "identifier": str(self.identifier),
            "username": str(self.username),
            "firstname": str(self.firstname),
            "lastname": str(self.lastname),
            "email": str(self.email),
            "expires": str(self.expires),
            "created": str(self.created),
            "sclass": str(self.sclass),
            "type": str(self.type),
            "owned_objects": str(self.owned_objects),
            "owned_payments": str(self.owned_payments),
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
    type: str = "ClassHead"

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
    author: str | Student | ClassHead
    target: str | list[str] # Student ID, Class ID
    product: Any = None
    cost: float
    iban: str
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

# API Schemas

class APIinit(BaseModel): 
    access_token: str
    only_students: bool = False 
    only_admins: bool = False

    def return_dict(self):
        return {
            "access_token": self.access_token,
        }
        
class APIDefault(BaseModel):
    access_token: str
    


    def return_dict(self):
        return {
            "access_token": self.access_token,
        }

class APIPayment(APIDefault):
    name: str
    author: str
    target: str #Student | SClass | list[Student|SClass]
    product: Any = None
    cost: float
    iban: str
    start_date: datetime = datetime.now
    due_date: datetime
    expires: datetime = datetime.now() + timedelta(days=365)
