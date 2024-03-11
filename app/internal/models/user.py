# from sqlalchemy.orm import declarative_base
# from sqlalchemy import Column, Integer, String

# Base = declarative_base()

# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String,)
#     user_type = Column(String)

from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    user_name: str
    user_type: str

class User(UserBase, table=True):
    id: str = Field(default=None, nullable=False, primary_key=True)

class UserCreate(UserBase):
    pass
