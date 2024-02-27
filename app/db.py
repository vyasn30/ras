import os

from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv



DATABASE_URL = os.environ.get("DATABASE_URL") # For docker
DATABASE_URL = os.environ.get("DATABASE_URL_LOCAL") # For local

engine = create_async_engine(DATABASE_URL, echo=True)

# Async session maker
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session():
    async with async_session() as session:
        yield session