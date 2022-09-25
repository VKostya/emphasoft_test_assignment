from datetime import timedelta
from fastapi import APIRouter, Body, HTTPException, Depends
from db.database import auth_users
from schemas.schemas import AuthModel
from utils.auth import create_access_token, get_password_hash, verify_password
from config import config
from fastapi.security import OAuth2PasswordRequestForm

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
def create_auth_token(
    auth_form: OAuth2PasswordRequestForm = Depends(),
):
    user = auth_users.find_one({"username": auth_form.username})
    if not user:
        raise HTTPException(status_code=401, detail="This user does not exist")
    if not verify_password(
        plain_password=auth_form.password, hashed_password=user["password"]
    ):
        raise HTTPException(status_code=401, detail="Wrong password")
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
