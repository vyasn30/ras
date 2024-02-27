from fastapi import APIRouter, Depends
from uuid import UUID, uuid4
from fastapi.responses import JSONResponse
from db import get_session
from internal.models.user import User, UserBase, UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

user_router = APIRouter(prefix="/users")
users = {}

# @user_router.get("/{user_id}")
# async def read_user(user_id: UUID):
#     # try:
#         payload = {
#         "user_id": str(user_id),
#         "user_name": str(users.get(str(user_id)).get("name"))
#         } 

#         return JSONResponse(
#             status_code=200,
#             content=payload
#         )

    # except Exception as e:
    #     return JSONResponse(
    #         status_code=404,
    #         content={"message": "User not found"}
    #     )

@user_router.post("/")
async def create_user(user: UserCreate, session:AsyncSession = Depends(get_session)):
    try:
        user_id = uuid4()
        new_user = User(
            user_name=user.user_name,
            user_type=user.user_type,
            id=str(user_id)
        )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user) 
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


@user_router.get("/", response_model=list[UserBase])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return [
        User(
                user_name=user.user_name,
                user_type=user.user_type,
            )
        for user in users
    ]