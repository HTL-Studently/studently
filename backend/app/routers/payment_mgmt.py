# Endpoints for creating and managing payments for the administration

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

@router.post("/payment", tags=["Payments"])
async def create_payment(data: APIPayment):
    """Create and assign a payment object"""

    response = await logic.authorize_user(request)
    try:
        user = response["success"]["user"]
    except Exception as error:
       raise HTTPException(status_code=403, detail=f"Authorization failed - {error}")
    

    
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


@router.put("/payment", tags=["Payments"])
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


@router.get("/payment", tags=["Payments"])
async def get_payment(data: APIDefault):
    access_token = data.access_token

    graph_user = await graph.get_user_account(access_token=access_token)
    user = await auth_user(graph_user=graph_user, access_token=access_token)

