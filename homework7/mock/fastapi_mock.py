from fastapi import Request, Response, FastAPI
from pydantic import BaseModel
import requests
import settings
from typing import Optional

app = FastAPI()


SURNAME_DATA = {'Kostya': 'Volkov', 'Olya': 'OLOLOEVA'}


@app.get('/get_surname/{name}', status_code=200)
def get_user_surname(response: Response, name: str):
    if surname := SURNAME_DATA.get(name):
        return surname
    else:
        response.status_code = 404
        return f'Surname for user "{name}" not found'
