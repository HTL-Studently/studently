import os
import uuid
from datetime import datetime, timedelta
from typing import Annotated, Optional, Union, Literal, Any
from fastapi import Depends, FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel
from dotenv import load_dotenv
import json
from jose import jwt
import bson.binary
from app.db.schemas import (
    Student,
    Payment,
    Token,
    License,
    APIinit,
    LicenseGroup,
    APIDefault,
    APIPayment,
    PaymentConfirmation,
    APISearch,
    APIPaymentUpdate,
)
from app.logic import Logic
from app.db.mongo import MongoDB
from app.graph.graph import GraphAPI
from app.api import api_logic


# TODO

# Split API Endpoints into multiple files
# https://fastapi.tiangolo.com/tutorial/bigger-applications/


print("Welcome to Studently")

# API Variables

load_dotenv()
CONTACT_NAME = str(os.environ.get("CONTACT_NAME"))
CONTACT_EMAIL = str(os.environ.get("CONTACT_EMAIL"))
STARTUP_ADMIN_USER = str(os.environ.get("STARTUP_ADMIN_USER"))
STARTUP_ADMIN_PASSWD = str(os.environ.get("STARTUP_ADMIN_PASSWD"))
STARTUP_ADMIN_EMAIL = str(os.environ.get("STARTUP_ADMIN_EMAIL"))


graph = GraphAPI()
db = MongoDB()
logic = Logic()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
description = ""

with open("./README.md") as file:
    description = file.read()

tags_metadata = api_logic.tags_metadata

# API

app = FastAPI(
    openapi_tags=tags_metadata,
    redoc_url=None,
    title="StudentlyAPI",
    description=description,
    summary="Studently Backend API",
    version="0.0.1",
    contact={
        "name": CONTACT_NAME,
        "emial": CONTACT_EMAIL,
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def auth_user(graph_user, access_token: str):
    # try:
    id = graph_user["id"]

    db_student = db.read_student(search_par="identifier", search_val=id)

    if not db_student:
        data = APIinit(access_token=access_token)
        await initialize_db(
            data
        )  # Replace with faster function that only handles individual user
        db_student = db.read_student(search_par="identifier", search_val=id)

    if type(db_student) == list:
        db_student = db_student[0]

    if db_student:

        # Makes sure that these fields are lists
        # Quick fix, could be better
        if type(db_student["owned_objects"]) == str:
            db_student["owned_objects"] = []
        if type(db_student["owned_payments"]) == str:
            db_student["owned_payments"] = []

        user = Student(
            disabled=db_student["disabled"],
            identifier=db_student["identifier"],
            username=db_student["username"],
            firstname=db_student["firstname"],
            lastname=db_student["lastname"],
            email=db_student["email"],
            expires=db_student["expires"],
            created=db_student["created"],
            sclass=db_student["sclass"],
            type=db_student["type"],
            owned_objects=db_student["owned_objects"],
            owned_payments=db_student["owned_payments"],
        )

        return user
    else:
        return False

    # except Exception  as e:
    #     print(f"Authentication user failed: \n {e}")
    #     return False


######### Test Endpoints #########


@app.get("/", tags=["Test"])
async def root_api():
    return "Welcome to the Studently API"


# Test Endpoint
@app.get("/test", tags=["Test"])
async def test_api():
    return "Pong"


######### Login Endpoints #########


# Initiate Database
@app.post("/initdb", tags=["initdb"])
async def initialize_db(data: APIinit):
    access_token = data.access_token

    users = await logic.graph_get_all_students(access_token)
    all_students = users["all_students"]
    all_sclass = users["all_sclass"]
    all_classHeads = users["all_classHeads"]

    db.create_student(all_students)
    db.create_classHead(all_classHeads)
    db.create_sclass(all_sclass)

    return {
        "message": {
            "all_students": all_students,
            "all_classHeads": all_classHeads,
            "all_sclass": all_sclass,
        }
    }


# Get a (sorted) list of students
@app.get("/students", tags=["initdb"])
async def getStudentList(sclass: str = ""):

    if sclass:
        all_students = db.read_student(search_par="sclass", search_val=sclass)
        return all_students

    all_students = db.read_student()
    return {"message": all_students}


# Create a license group
@app.post("/licgroup", tags=["Licenses"])
async def create_license_group(lic_group: LicenseGroup):
    new_group = LicenseGroup(
        identifier=lic_group.identifier,
        license_name=lic_group.license_name,
        description=lic_group.description,
        cost=lic_group.cost,
        expires=lic_group.expires,
        licenses=lic_group.licenses,
    )

    created = db.create_license_group(licenses_group=new_group)


@app.post("/license", tags=["Licenses"])
async def create_license(license: License):
    new_license = License(
        disabled=license.disabled,
        identifier=license.identifier,
        license_name=license.license_name,
        license_group=license.license_group,
        description=license.description,
        cost=license.cost,
        expires=license.expires,
        created=license.created,
    )

    created = db.create_license([new_license])


######### Frontend Student Endpoints #########


@app.post("/profile", tags=["Profile"])
async def get_profile(data: APIDefault):
    access_token = data.access_token

    graph_user = await graph.get_user_account(access_token=access_token)
    user = await auth_user(graph_user=graph_user, access_token=access_token)

    if user:
        response = {
            "code": 200,
            "message": {
                "profile": user,
                # "pfp": user_pfp,
            },
        }

    else:
        response = {
            "code": 403,
            "message": {
                "error": "User not found",
            },
        }

    return response


@app.post("/confirmpay", tags=["Payments"])
async def confirm_payment(file: UploadFile):
    # access_token = data.access_token

    # graph_user = await graph.get_user_account(access_token=access_token)
    # user = auth_user(graph_user=graph_user)

    # Discard non pdf files
    if file.content_type != "application/pdf":
        response = {
            "code": "400",
            "message": {"error": "Wrong filetype - only pdfs are allowed"},
        }
    else:

        payment = "EINSZWEIDREI"

        file_content = await file.read()
        file_binary = bson.binary.Binary(file_content)

        payment_confirmation = PaymentConfirmation(
            disabled=False,
            identifier=str(uuid.uuid4()),
            author="ERIK",  # user["identifier"],
            payment=payment,
            expires=datetime.now() + timedelta(days=3000),
            created=datetime.now(),
            file_name=file.filename,
            filedata=file_binary,
        )

        insert = db.add_payment_confirmation(payment_confirmation=payment_confirmation)

        response = {
            "code": "201",
            "message": f"Paymentconfiguration {file.filename} uploaded successfully",
        }

        await file.close()

    return response


######### Frontend ClassHead Endpoints #########


@app.post("/payment", tags=["Payments"])
async def create_payment(data: APIPayment):
    access_token = data.access_token

    graph_user = await graph.get_user_account(access_token=access_token)
    user = await auth_user(graph_user=graph_user, access_token=access_token)

    if user.type != "ClassHead":
        print("Payment created by Student")

    # Assign payment to users
    sclass = db.read_sclass(name=data.target)
    student = db.read_student(search_par="identifier", search_val=data.target)

    if sclass:
        student_list = db.read_student(search_par="sclass", search_val=sclass["name"])

        author = user.__dict__
        payment = Payment(
            disabled=data.disabled,
            id=str(uuid.uuid4()),
            name=data.name,
            author=str(author["identifier"]),
            target=str(data.target),
            product=data.product,
            confirmation=None,
            payed=False,
            cost=data.cost,
            iban=data.iban,
            bic=data.bic,
            start_date=data.start_date,
            due_date=data.due_date,
            expires=data.expires,
        )
        dict_payment = payment.__dict__

        for student in student_list:
            update = db.update_student(
                id=student["identifier"],
                field="owned_payments",
                value=dict_payment,
                update_type="push",
            )

        insert = str(db.create_payment(payment=payment))

        return {
            "code": 200,
            "message": update,
        }

    elif student:
        update = db.update_student(
            id=student["identifier"],
            field="owned_payments",
            value=dict_payment,
            update_type="push",
        )

        insert = str(db.create_payment(payment=payment))

        return {
            "code": 200,
            "message": update,
        }

    else:
        return {
            "code": 400,
            "message": "Target must be a valid Class",
        }



@app.put("/payment", tags=["Payments"])
async def update_payment(data: APIPaymentUpdate):
    access_token = data.access_token

    graph_user = await graph.get_user_account(access_token=access_token)
    user = await auth_user(graph_user=graph_user, access_token=access_token)

    if user.type != "ClassHead":
        print("Payment created by Student")

    student = db.read_student(search_par="identifier", search_val=data.target)
    if type(student) == list and not []:
        student = student[0]
    
    # Add new payment entry
    author = user.__dict__
    payment = Payment(
        disabled=data.disabled,
        id=data.id,
        name=data.name,
        author=author["identifier"],
        target=data.target,
        product=data.product,
        confirmation=data.confirmation,
        payed=data.payed,
        cost=data.cost,
        iban=data.iban,
        bic=data.bic,
        start_date=data.start_date,
        due_date=data.due_date,
        expires=data.expires,
    )
    dict_payment = payment.__dict__

    # Delete old payment entry and add new one
    owned_payments = student["owned_payments"]
    for payment in owned_payments:
        if payment["id"] == data.id:
            owned_payments.remove(payment)
            break

    owned_payments.append(dict_payment)    

    # Reset payment entries (DB)
    db.update_student(id=data.target, field="owned_payments", value=[], update_type="set")

    # Readd payment entries
    update = db.update_student(
        id=student["identifier"],
        field="owned_payments",
        value=owned_payments,
        update_type="set",
    )

    return {
        "code": 200,
        "message": update,
    }


@app.get("/payment", tags=["Payments"])
async def get_payment(data: APIDefault):
    access_token = data.access_token

    graph_user = await graph.get_user_account(access_token=access_token)
    user = await auth_user(graph_user=graph_user, access_token=access_token)


@app.post("/class")
async def get_class(data: APISearch):
    access_token = data.access_token

    graph_user = await graph.get_user_account(access_token=access_token)
    user = await auth_user(graph_user=graph_user, access_token=access_token)

    if not user:
        return {"code": 403, "message": "This user does not exist"}

    if user.type != "ClassHead":
        print("Class accessed by Student")

    result = db.read_student(search_par="sclass", search_val=data.search_value)

    print(result)

    response = {"code": 200, "message": result}

    return response



