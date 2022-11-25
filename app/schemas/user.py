from typing import Optional
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class UserSchema(BaseModel):
    id: int
    fullname: str
    username: str
    gender: Gender

    class Config:
        orm_mode = True


class UserUpdateDTO(BaseModel):
    fullname: Optional[str] = None
    username: Optional[str] = None
    gender: Optional[str] = None
