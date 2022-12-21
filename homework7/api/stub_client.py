from api.base_api import BaseApi
import settings


class StubApiClient(BaseApi):
    def __init__(self):
        super().__init__()
        self.base_url = f'http://{settings.STUB_HOST}:{settings.STUB_PORT}'

    def get_age(self, name):
        res = self._request('GET', f'/get_age/{name}')
        return res.json
