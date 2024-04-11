# Endpoints to fetch students by name, class, etc
from fastapi import APIRouter, Request, Response, status, HTTPException

from app.graph.graph import GraphAPI 
from app.logic import Logic
from app.db.mongo import MongoDB

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

graph = GraphAPI()
db = MongoDB()
logic = Logic()

router = APIRouter()

@router.get("/students", tags=["Profile"])
async def get_profile(request: Request, full_list: bool = False, sclass: str = "", id: str = ""):

    response = await logic.authorize_user(request)
    try:
        user = response["success"]["user"]
    except Exception as error:
       raise HTTPException(status_code=403, detail=f"Authorization failed - {error}")

    if full_list:
        all_students = db.read_student()
        return {"message": all_students}
    elif sclass:
        all_students = db.read_student(search_par="sclass", search_val=sclass)
        return {"message": all_students}
    elif id:
        all_students = db.read_student(search_par="identifier", search_val=id)
        return {"message": all_students}
    else:
        return {"message": user}
