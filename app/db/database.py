from pymongo import mongo_client
from config import config

client = mongo_client.MongoClient(config.DATABASE_URL)
db = client[config.MONGO_DB]

auth_users = db.auth_users
users = db.users


def read_user(user):
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "is_active": user["is_active"],
    }
