import httpx
from fastapi.testclient import TestClient
from main import app 
import asyncio

client = TestClient(app)

all_users = dict()

def test_root():
    response = client.get("/index")
    assert response.status_code == 200

async def async_test_create_users(n_user: int):
    async with httpx.AsyncClient() as async_client:
        tasks = []

        for i in range(n_user):
            user_name = f"user_{i}"
            payload = {
                "name": user_name,
                "type": "user"
            }
            url = "http://localhost:8000/users/"

            tasks.append(async_client.post(url, json=payload)) 
        
        responses = await asyncio.gather(*tasks)

        for response in responses:
            assert response.status_code == 200


async def async_test_get_all_users(n_users):
    async with httpx.AsyncClient() as async_client:
        tasks = []
        url = "http://localhost:8000/users/"

        tasks.append(async_client.get(url))

        response = await asyncio.gather(*tasks)
        
        all_users = response[0].json()

        assert n_users == len(response[0].json())

        

async def async_test_get_user_by_id():
    async with httpx.AsyncClient() as async_client:
        tasks = []
        
        url = "http://localhost:8000/users/"
        for id in all_users:
            tasks.append(async_client.get(url+id)) 
        
        responses = await asyncio.gather(*tasks)

        for response in responses:
            assert response.status_code == 200


n_users = 100

asyncio.run(async_test_create_users(n_users))
asyncio.run(async_test_get_all_users(n_users))
asyncio.run(async_test_get_user_by_id())