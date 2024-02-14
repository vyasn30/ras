from fastapi import APIRouter 
from uuid import UUID, uuid4
from app.internal.schema.user import User, UserCreate
from app.internal.schema.question import Question, QuestionCreate
from fastapi.responses import JSONResponse

user_router = APIRouter(prefix="/users")
users = {}

@user_router.get("/{user_id}")
async def read_user(user_id: UUID):
    # try:
        payload = {
        "user_id": str(user_id),
        "user_name": str(users.get(str(user_id)).get("name"))
        } 

        return JSONResponse(
            status_code=200,
            content=payload
        )

    # except Exception as e:
    #     return JSONResponse(
    #         status_code=404,
    #         content={"message": "User not found"}
    #     )

@user_router.post("/")
async def create_user(user: UserCreate):
    try:
        user_id = uuid4()
        new_user = User(
            name=user.name,
            type=user.type,
            id=str(user_id)
        )
        users[str(user_id)] = new_user.model_dump()
        return JSONResponse(
            content={
                "message": f"User created with id: {str(user_id)}"
            },
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(
            content={"message": "Unknon error in creating user"},
            status_code=500
        )

@user_router.get("/")
def read_all_users():
    return users