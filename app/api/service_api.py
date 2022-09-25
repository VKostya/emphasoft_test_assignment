from fastapi import APIRouter, Body
from db.database import users
import pymongo

service_router = APIRouter()


@service_router.get("/users", tags=["service"])
def greet():
    return {"data": users.find()}
