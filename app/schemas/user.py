from pydantic import BaseModel, EmailStr
from typing import Literal

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: Literal["admin"]

    class Config:
        orm_mode = True
