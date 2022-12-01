from fastapi import FastAPI
import random

app = FastAPI()


@app.get('/get_age/{name}')
def get_user_age(name):
    return random.randint(18, 105)
