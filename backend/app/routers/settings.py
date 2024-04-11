# Endpoints to get and set settings
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