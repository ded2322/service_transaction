from typing import Optional

from pydantic import BaseModel, EmailStr


class UserDataRegisterSchema(BaseModel):
    name: str
    password: str
    email: EmailStr


class UserDataLoginSchema(BaseModel):
    name: str
    password: str
    email: EmailStr


class JWTTokenSchema(BaseModel):
    token: str


class UserUpdateDataSchema(BaseModel):
    password: str
