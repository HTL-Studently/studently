import os
import uuid
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, File, UploadFile, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import json
import bson.binary
from app.db.schemas import (
    Student,
    Payment,
    License,
    APIinit,
    LicenseGroup,
    API,
    APIDefault,
    APIPayment,
    PaymentConfirmation,
    APIStudent,
    APIPaymentUpdate,
)
from app.logic import Logic
from app.db.mongo import MongoDB
from app.graph.graph import GraphAPI
from app.api import api_logic

from app.routers import students


print("Welcome to Studently")

# API Variables
custom_adobe_group = "c4159660-7ef8-4a79-9332-184b75896e8a"

adobe_license = LicenseGroup(
    disabled = False,
    identifier = "adobeDefaultLicense",
    license_name = "AdobeLicense",
    description = "Adobe Default License",
    cost = "5€",
    source = "680033ff-1040-43a8-a8db-18d8d6e81f9a",
)

defaultLicense = [adobe_license]

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

# Student Endpoints
app.include_router(students.router)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Adjust this to match your SvelteKit app's origin
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

    # return await logic.initialize_db(access_token)
    return await logic.initialize_db(access_token)

    # # Get students and teachers from GraphAPI
    # users = await logic.graph_get_all_students(access_token)
    # all_students = users["all_students"]
    # all_sclass = users["all_sclass"]
    # all_classHeads = users["all_classHeads"]

    # #  Write students and teachers to database
    # db.create_student(all_students)
    # db.create_classHead(all_classHeads)
    # db.create_sclass(all_sclass)

    # # Assign default licenses
    # for group in defaultLicense:
    #     await logic.assign_license_to_msgroup(access_token=access_token, license_group=group)

    # return {
    #     "message": {
    #         "all_students": all_students,
    #         "all_classHeads": all_classHeads,
    #         "all_sclass": all_sclass,
    #     }
    # }


# Get a (sorted) list of students
# @app.get("/students", tags=["initdb"])
# async def getStudentList(sclass: str = ""):

#     if sclass:
#         all_students = db.read_student(search_par="sclass", search_val=sclass)
#         return all_students

#     all_students = db.read_student()
#     return {"message": all_students}


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
async def get_profile(request: Request):

    authorization_header = request.headers.get("authorization")
    if authorization_header:
        access_token = authorization_header[len("Bearer "):]
    else:
        # If the Authorization header is not present, try to get the token from the cookie
        access_token = request.cookies.get("accessToken")

    print(access_token)

    if access_token is None:
        return {"error": "Authorization header is missing"}

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
async def confirm_payment(file: UploadFile = File(...), payment: str = Form(...), id: str = Form(...), sclass: str = Form(...)):

    # Discard non pdf files
    if file.content_type != "application/pdf":
        response = {
            "code": "400",
            "message": {"error": "Wrong filetype - only pdfs are allowed"},
        }
    else:

        file_contents = await file.read()

        payment_confirmation = PaymentConfirmation(
            disabled=False,
            identifier=str(uuid.uuid4()),
            author=id,
            sclass = sclass,
            expires=datetime.now() + timedelta(days=3000),
            created=datetime.now(),
            file_name=file.filename,
            filedata=file_contents,
        )

        insert = db.add_payment_confirmation(payment_confirmation=payment_confirmation)

        response = {
            "code": "201",
            "message": f"Paymentconfiguration {file.filename} uploaded successfully",
        }

        await file.close()

    return response

@app.get("/confirmpay", tags=["Payments"])
async def get_confirmation():
    pass

######### Frontend ClassHead Endpoints #########




######### Class list Endpoints #########


@app.post("/class")
async def get_class(request: Request):
    authorization_header = request.headers.get("authorization")
    access_token = authorization_header[len("Bearer "):]

    if access_token is None:
        return {"error": "Authorization header is missing"}

    graph_user = await graph.get_user_account(access_token=access_token)
    user = await auth_user(graph_user=graph_user, access_token=access_token)

    if not user:
        return {"code": 403, "message": "This user does not exist"}

    if user.type != "ClassHead":
        print("Class accessed by Student")

    #result = db.read_student(search_par="sclass", search_val=data.search_value)

    result = db.read_sclass()

    return {"code": 200, "message": result}


@app.post("/student")
async def get_students(data: APIStudent):
    access_token = data.access_token
    search_par = data.search_par
    search_val = data.search_val

    graph_user = await graph.get_user_account(access_token=access_token)
    user = await auth_user(graph_user=graph_user, access_token=access_token)

    if not user:
        return {"code": 403, "message": "This user does not exist"}

    if user.type != "ClassHead":
        print("Class accessed by Student")

    return db.read_student(search_par=search_par, search_val=search_val)