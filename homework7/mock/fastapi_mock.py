from fastapi import Request, Response, FastAPI


app = FastAPI()


SURNAME_DATA = {}


@app.get('/get_surname/{name}', status_code=200)
def get_user_surname(response: Response, name: str):
    if surname := SURNAME_DATA.get(name):
        return surname
    else:
        response.status_code = 404
        return f'Surname for user {name} not found'


@app.put("/surname/{name}")
async def put_user_surname(request: Request, name: str):
    body = await request.json()
    SURNAME_DATA[name] = body.get('surname')
    return 'success'


@app.delete("/surname/{name}")
def delete_user_surname(name: str):
    try:
        del SURNAME_DATA[name]
    except KeyError:
        return 'surname doesnt exist'
    return 'success'
