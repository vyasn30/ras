import httpx
from app.main import app 
import asyncio

async def async_test_create_question():
    async with httpx.AsyncClient() as async_client:
        tasks = []

        payload_user = {
            "name": "test_user",
            "type": "user"
        }

        url_user = "http://localhost:8000/users/"

        tasks.append(
            async_client.post(url_user, json=payload_user)
        )

        url_question = "http://localhost:8000/"