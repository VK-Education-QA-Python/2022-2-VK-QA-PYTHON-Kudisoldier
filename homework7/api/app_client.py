from api.base_api import BaseApi
import settings


class AppApiClient(BaseApi):
    def __init__(self):
        super().__init__()
        self.base_url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'

    def add_user(self, name):
        resp = self._request('POST', '/add_user', json={'name': name})
        if resp.status_code == 201:
            return resp.json['user_id']
        else:
            return resp.status_code

    def get_user(self, name, field_name):
        resp = self._request('GET', f'/get_user/{name}')
        if resp.status_code == 200:
            return resp.json[field_name]
        else:
            return resp.status_code
