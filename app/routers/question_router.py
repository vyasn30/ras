from fastapi import APIRouter
from uuid import UUID, uuid4
from internal.schema.user import User, UserCreate
from internal.schema.question import Question, QuestionCreate
from fastapi.responses import JSONResponse

questions = dict()

question_router = APIRouter(prefix="/questions")


@question_router.post("/")
async def create_question(req_question: QuestionCreate):
    try:
        question_id = uuid4()
        question = Question(
            content=req_question.content,
            id=str(question_id)
        )
    
        questions[str(question_id)] = question.model_dump()

        return JSONResponse(
            content={
                "message": f"Question created with id: {question_id}"
            },
            status_code=200
        )

    except Exception as e:
        return JSONResponse(
            content={"message": "Unknown error in creating question"},
            status_code=500
        )


@question_router.get("/questions/{question_id}")
async def read_question(question_id: str):
    try:
        payload = {
            "question_id": question_id,
            "question" : questions.get(question_id).get("content")
        }
        print(questions)
        return JSONResponse(
            content=payload,
            status_code=200,
        )

    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=404,
            content={"message": "Question not found"}
        )
 
