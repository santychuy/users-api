from typing import Optional
from uuid import uuid4, UUID
from pydantic import BaseModel, validator
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class UserSchema(BaseModel):
    id: int
    fullname: str
    username: str

    class Config:
        orm_mode = True


class UserUpdateDTO(BaseModel):
    fullname: Optional[str] = None
    username: Optional[str] = None
