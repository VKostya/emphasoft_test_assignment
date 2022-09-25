from fastapi import APIRouter, Body, HTTPException, Depends
from schemas.schemas import AuthUser, MultipleReadUser, ReadUser, WriteUser
from utils.auth import get_current_user, get_password_hash
from db.database import read_user, users
from bson.objectid import ObjectId

service_router = APIRouter()

""""
@service_router.get("/users", tags=["service"], response_model=MultipleReadUser)
def get_all_users(current_user: AuthUser = Depends(get_current_user)):
    return users.find()
"""


@service_router.get("/users/{id}", tags=["service"], response_model=ReadUser)
def get_user_by_id(id: str, current_user: AuthUser = Depends(get_current_user)):
    print(users.find_one({"_id": ObjectId(id)}))
    return read_user(users.find_one({"_id": ObjectId(id)}))


@service_router.post("/users", tags=["service"], response_model=ReadUser)
def add_user(
    user: WriteUser = Body(..., embed=True),
    current_user: AuthUser = Depends(get_current_user),
):
    user = users.insert_one(
        {
            "username": user.username,
            "password": get_password_hash(user.password),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_active": user.is_active,
        }
    )
    new_user = users.find_one({"_id": user.inserted_id})
    return read_user(new_user)


"""
@service_router.patch("/users/{id}", tags=["service"], response_model=ReadUser)
def update_user(
    id: str,
    user: WriteUser = Body(..., embed=True),
    current_user: AuthUser = Depends(get_current_user),
):
    return {""}


@service_router.delete("/users/{id}", tags=["service"])
def delete_user(id: str, current_user: AuthUser = Depends(get_current_user)):
    return {}
"""
