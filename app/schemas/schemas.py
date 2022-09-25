from xmlrpc.client import boolean
from pydantic import BaseModel


class AuthModel(BaseModel):
    username: str
    password: str


class AuthUser(BaseModel):
    username: str


class WriteUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str
    is_active: boolean


class ReadUser(BaseModel):
    id: str
    username: str
    first_name: str
    last_name: str
    is_active: str


class MultipleReadUser(BaseModel):
    data: list[ReadUser]
