from pymongo import mongo_client
from utils.security import get_password_hash
from config import config
from bson.objectid import ObjectId
from fastapi import HTTPException

client = mongo_client.MongoClient(config.DATABASE_URL)
db = client[config.MONGO_DB]

auth_users = db.auth_users
users = db.users


def read_user(user):
    """
    funcion to read db document
    """
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "is_active": user["is_active"],
    }


def write_user(user):
    return {
        "username": user.username,
        "password": get_password_hash(user.password),
        "first_name": user.first_name,
        "last_name": user.last_name,
        "is_active": user.is_active,
    }


def validate_user(id):
    user = users.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(status_code=404, detail="This user does not exist")
