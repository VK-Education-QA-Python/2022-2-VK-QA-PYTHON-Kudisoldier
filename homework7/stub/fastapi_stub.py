from fastapi import Request, Response, FastAPI
from pydantic import BaseModel
import requests
import settings
from typing import Optional
import random

app = FastAPI()


@app.get('/get_age/{name}')
def get_user_age(name):
    return random.randint(18, 105)

