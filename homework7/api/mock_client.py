from api.base_api import BaseApi
import settings


class MockApiClient(BaseApi):
    def __init__(self):
        super().__init__()
        self.base_url = f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}'
        self.logging = True

    def add_surname(self, name, surname):
        res = self._request('PUT', f'/surname/{name}', json={'surname': surname})
        return res.json

    def get_surname(self, name):
        res = self._request('GET', f'/get_surname/{name}')
        return res.json

    def delete_surname(self, name):
        res = self._request('DELETE', f'/surname/{name}')
        return res.json
