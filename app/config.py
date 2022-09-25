from distutils.command.config import config
from pydantic import BaseSettings


class Config(BaseSettings):
    DATABASE_URL: str  # MongoDB connection URL
    MONGO_DB: str  # Mongo database
    SECRET_KEY: str  # secret key for jwt encoding
    ALGORITHM: str

    class Config:
        env_file = ".env"


config = Config()
