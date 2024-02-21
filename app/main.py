from fastapi import FastAPI
from routers.user_router import user_router
from routers.question_router import question_router

app = FastAPI()
app.include_router(user_router)
app.include_router(question_router)

@app.get("/index")
async def index():
    return {"jsca"}
   