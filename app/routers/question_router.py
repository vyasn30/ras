from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from uuid import UUID, uuid4
from typing import List

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import query
from sqlmodel import select
from db import get_session
from internal.models.query import Query, QueryBase, QueryCreate


query_router = APIRouter(prefix="/query")

# USER_ID is being passed here, refactor it being passed with cookies when user is logged in
@query_router.post("/{current_user_id}")
async def create_query(req_query: QueryCreate, current_user_id:UUID, session:AsyncSession = Depends(get_session)):
    try:
        query_id = str(uuid4())
        new_query = Query(
            query_content=req_query.content,
            id = query_id,
            user_id = str(current_user_id)
        )
        
        # Add later: check if user exists, else exception 
        session.add(new_query)


        # Should not return queryID when in PRod
        return JSONResponse(
            content={
                "message": f"query created with id: {query_id}"
            },
            status_code=200
        )

    except Exception as e:
        return JSONResponse(
            content={"message": "Unknown error in creating query"},
            status_code=500
        )


@query_router.get("{current_user_id}", response_model=List[QueryBase])
async def read_all_queries_for_user(
        current_user_id:UUID, 
        session:AsyncSession=Depends(get_session)
    ):
    results = session.execute(
            select(Query)
            .where(Query.user_id==str(current_user_id))
        )
    return results
#
#@query_router.get("{user_id}/{query_id}")
#async def read_query(query_id: UUID, user_id:UUID, session:AsyncSession=Depends(get_session)):
#    try:
#
#        payload = {
#            "query_id": query_id,
#            "query" : querys.get(query_id).get("content")
#        }
#        print(querys)
#        return JSONResponse(
#            content=payload,
#            status_code=200,
#        )
#
#    except Exception as e:
#        print(e)
#        return JSONResponse(
#            status_code=404,
#            content={"message": "query not found"}
#        )
#

async def read_user(user_id: UUID, session: AsyncSession = Depends(get_session)):
    user_info = await session.execute(select(User).filter(User.id == str(user_id)))
    user = user_info.scalars().first()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")
