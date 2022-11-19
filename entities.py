from typing import Optional
from uuid import uuid4, UUID
from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    fullname: str
    username: str
    created_date: Optional[datetime] = datetime.now()
    gender: Gender


class UserUpdateDTO(BaseModel):
    fullname: Optional[str]
    username: Optional[str]
    gender: Optional[Gender]
