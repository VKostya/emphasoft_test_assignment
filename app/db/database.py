from pymongo import mongo_client
from config import config

client = mongo_client.MongoClient(config.DATABASE_URL)
db = client[config.MONGO_DB]

auth_users = db.auth_users
users = db.users
