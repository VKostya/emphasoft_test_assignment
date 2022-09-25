from fastapi import APIRouter, Body, HTTPException
from db.database import auth_users
from schemas.schemas import AuthModel
from utils.auth import get_password_hash, verify_password

auth_router = APIRouter()


@auth_router.post("/signup", summary="Create API's user", tags=["auth"])
def create_new_user(auth_form: AuthModel = Body(..., embed=True)):
    user = auth_users.find_one({"username": auth_form.username})
    if user:
        raise HTTPException(status_code=401, detail="This user already exists")
    try:
        auth_users.insert_one(
            {
                "username": auth_form.username,
                "password": get_password_hash(auth_form.password),
            }
        )
    except:
        raise HTTPException(status_code=502, detail="DB insert error")
    return {"data": "you have signed up"}


@auth_router.post("/login", summary="create auth-token", tags=["auth"])
def create_auth_token(auth_form: AuthModel = Body(..., embed=True)):
    return {"token": "token"}
