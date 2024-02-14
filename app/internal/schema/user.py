from pydantic import BaseModel
from enum import Enum
from uuid import UUID
from typing import Optional

class UserType(str, Enum):
    admin = "admin",
    user = "user"

class UserCreate(BaseModel):
    name: str
    type: UserType

class User(UserCreate):
    id: UUID
