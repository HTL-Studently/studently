from datetime import datetime, timedelta
import json
from pydantic import BaseModel
import uuid
from typing import Literal, Any
from decimal import Decimal
from typing import List


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
    identifier: str
    name: str

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
    disabled: bool
    id: str = str(uuid.uuid4())
    name: str
    author: str | Student | ClassHead
    target: str | list[str] # Student ID, Class ID
    product: Any = None
    confirmation: str | None
    payed: bool = False
    cost: float
    iban: str
    bic: str
    start_date: datetime = datetime.now()
    due_date: datetime
    expires: datetime = datetime.now() + timedelta(days=365)

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


class Product(BaseModel):
    disabled: bool
    name: str
    author: list[str] # IDs
    target: str | list[str] # Student ID, Class ID
    info: Any = None
    confirmation: str = ""
    cost: float
    iban: str
    bic: str
    start_date: datetime = datetime.now()
    due_date: datetime
    expires: datetime = datetime.now() + timedelta(days=365)
    delete_date: datetime = datetime.now() + timedelta(days=365)


class StudentProduct(BaseModel):
    disabled: bool
    name: str
    author: str 
    info: Any = None
    confirmation: str
    confirmed: bool
    cost: float
    iban: str
    bic: str
    start_date: datetime = datetime.now()
    due_date: datetime
    expires: datetime = datetime.now() + timedelta(days=365)





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
    source: str = ""
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

class PaymentConfirmation(BaseModel):
    disabled: bool = False
    identifier: str
    author: str
    sclass: str
    expires: None | datetime = datetime.now() + timedelta(days=365)
    created: datetime = datetime.now()
    file_name: str
    filedata: Any

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

##### API Schemas #####
    
class API(BaseModel):
    access_token: str
    
class APISearch(API):
    search_value: str
    search_field: str | None = None

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
    disabled: bool = False
    name: str
    author: str
    target_type: str
    target: str #Student | SClass | list[Student|SClass]
    product: Any = None
    confirmation: str | None
    payed: bool = False
    cost: float
    iban: str
    bic: str
    start_date: datetime = datetime.now
    due_date: datetime
    expires: datetime = datetime.now() + timedelta(days=365)

class APIPaymentUpdate(APIPayment):
    id: str #Payment ID

class APIStudent(API):
    search_par: str
    search_val: str

class APIProduct(BaseModel):
    # disabled: bool
    # name: str
    # author: List[str] # ID List
    # target: List[str] # ID List
    # info: Any = None
    # cost: float
    # iban: str
    # bic: str
    # start_date: datetime = datetime.now()
    # due_date: datetime
    # expires: datetime = datetime.now() + timedelta(days=365)
    disabled: Any
    name: Any
    author: Any# ID List
    target: Any# ID List
    info: Any
    cost: Any
    iban: Any
    bic: Any
    start_date: Any
    due_date: Any
    expires: Any
    delete_date: Any