from pydantic import BaseSettings


class Config(BaseSettings):
    DATABASE_URL: str  # MongoDB connection URL
    MONGO_DB: str  # Mongo database
    SECRET_KEY: str  # secret key for jwt encoding
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"


config = Config()
