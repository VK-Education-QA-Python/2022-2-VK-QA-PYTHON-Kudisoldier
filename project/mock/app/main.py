from fastapi import Request, Response, FastAPI


app = FastAPI()


VKIDS = {'asdasd': 300}


@app.get('/vk_id/{username}', status_code=200)
def get_vk_id(response: Response, username: str):
    if vk_id := VKIDS.get(username):
        return {'vk_id': vk_id}
    else:
        response.status_code = 404
        return {}


@app.put("/vk_id/{username}", status_code=201)
async def put_vk_id(response: Response, request: Request, username: str):
    if VKIDS.get(username):
        response.status_code = 304
        return 'user exist'

    body = await request.json()
    VKIDS[username] = body.get('vk_id')
    return 'success'


@app.delete("/vk_id/{username}", status_code=204)
def delete_vk_id(response: Response, username: str):
    try:
        del VKIDS[username]
    except KeyError:
        response.status_code = 404
        return 'username doesnt exist'
    return 'success'
