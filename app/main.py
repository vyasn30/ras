from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers.user_router import user_router
from routers.question_router import query_router
from internal.models.user import User

from db import init_db

app = FastAPI()
app.include_router(user_router)
app.include_router(query_router)

@app.on_event("startup")
async def on_startup():
    print("Application startup --------------------")
    await init_db()
   
@app.get("/index")
async def index():
    return {"jsca"}
   
