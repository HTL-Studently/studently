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


class License():
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