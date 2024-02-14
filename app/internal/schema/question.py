from pydantic import BaseModel
from uuid import UUID

class QuestionCreate(BaseModel):
    content: str

class Question(QuestionCreate):
    id: UUID