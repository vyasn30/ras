from sqlmodel import SQLModel, Field
from uuid import UUID

class QueryBase(SQLModel):
    query_content: str

class Query(QueryBase, table=True):
    id: str = Field(
        default=None,
        nullable=False,
        primary_key=True
    )
    user_id: str = Field(
        default=None,
        nullable=False,
        foreign_key="user.id",
    )   

class QueryCreate(Query):
    pass
