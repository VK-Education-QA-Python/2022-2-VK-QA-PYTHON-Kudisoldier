from fastapi import Request, Response, FastAPI
from pydantic import BaseModel
import requests
import settings
from typing import Optional

app = FastAPI()


app_data = {}
user_id_seq = 1


class User(BaseModel):
    id: int
    name: str
    surname: Optional[str]
    age: Optional[int]


@app.post("/add_user", status_code=201)
async def create_user(response: Response, request: Request):
    global user_id_seq

    post_body = await request.json()
    user_name = post_body.get('name')
    if user_name not in app_data:
        app_data[user_name] = user_id_seq
        user_id_seq += 1
        return {'user_id': app_data[user_name]}
    else:
        response.status_code = 400
        return f'User_name {user_name} already exists: id: {app_data[user_name]}'


@app.get('/get_user/{name}', status_code=200)
def get_user_id_by_name(response: Response, name: str):
    if user_id := app_data.get(name):
        user = User(id=user_id, name=name)

        age_host = settings.STUB_HOST
        age_port = settings.STUB_PORT

        try:
            user.age = requests.get(f'http://{age_host}:{age_port}/get_age/{name}').json()
        except Exception as e:
            print(f'Unable to get age from external system:\n{e}')

        surname_host = settings.MOCK_HOST
        surname_port = settings.MOCK_PORT

        try:
            response_surname = requests.get(f'http://{surname_host}:{surname_port}/get_surname/{name}')
            if response_surname.status_code == 200:
                user.surname = response_surname.json()
        except Exception as e:
            print(f'Unable to get surname from external system:\n{e}')
        print(f'No surname found for user {name}')

        return user

    else:
        response.status_code = 404
        return f'User_name {name} not found'



# @app.put("/items/{item_id}")
# def update_item(item_id: int, user: User):
#     return {"item_name": user.name, "item_id": item_id}

