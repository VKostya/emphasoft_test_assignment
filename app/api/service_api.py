from fastapi import APIRouter, Body, HTTPException, Depends
from schemas.schemas import AuthUser, MultipleReadUser, ReadUser, WriteUser
from utils.auth import get_current_user
from db.database import read_user, users, validate_user, write_user
from bson.objectid import ObjectId

service_router = APIRouter()


@service_router.get("/users", tags=["service"], response_model=MultipleReadUser)
def get_all_users(current_user: AuthUser = Depends(get_current_user)):
    user_list = list()
    for user in users.find():
        user_list.append(read_user(user))
    return {"data": user_list}


@service_router.get("/users/{id}", tags=["service"], response_model=ReadUser)
def get_user_by_id(id: str, current_user: AuthUser = Depends(get_current_user)):
    validate_user(id)
    return read_user(users.find_one({"_id": ObjectId(id)}))


@service_router.post("/users", tags=["service"], response_model=ReadUser)
def add_user(
    user: WriteUser = Body(..., embed=True),
    current_user: AuthUser = Depends(get_current_user),
):
    user = users.insert_one(write_user(user))
    new_user = users.find_one({"_id": user.inserted_id})
    return read_user(new_user)


@service_router.patch("/users/{id}", tags=["service"], response_model=ReadUser)
def update_user(
    id: str,
    user: WriteUser = Body(..., embed=True),
    current_user: AuthUser = Depends(get_current_user),
):
    validate_user(id)
    users.update_one(
        {"_id": ObjectId(id)},
        {"$set": write_user(user)},
    )
    return read_user(users.find_one({"_id": ObjectId(id)}))


@service_router.delete("/users/{id}", tags=["service"], status_code=204)
def delete_user(id: str, current_user: AuthUser = Depends(get_current_user)):
    validate_user(id)
    users.delete_one({"_id": ObjectId(id)})
    return
