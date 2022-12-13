from api.base_api import BaseApi


class MockApiClient(BaseApi):
    def __init__(self):
        super().__init__()
        self.base_url = 'http://127.0.0.1:777/'

    def get(self, username):
        response = self._request('get', f'vk_id/{username}')
        return response

    def put(self, username, vk_id):
        data = {
            "vk_id": vk_id
        }

        response = self._request('put', f'vk_id/{username}', json=data)
        return response

    def delete(self, username):
        return self._request('delete', f'vk_id/{username}')
