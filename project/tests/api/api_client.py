from api.base_api import BaseApi


class ApiClient(BaseApi):
    def __init__(self):
        super().__init__()
        self.base_url = 'http://127.0.0.1:1000/'

    def add(self, name, surname, middle_name, username, password, email):
        data = {
            "name": name,
            "surname": surname,
            "middle_name": middle_name,
            "username": username,
            "password": password,
            "email": email
        }

        response = self._request('post', 'api/user', json=data)
        return response

    def reg(self, name, surname, middle_name, username, password, email):
        data = {
            "name": name,
            "surname": surname,
            "middle_name": middle_name,
            "username": username,
            "password": password,
            "email": email,
            "confirm": password,
            "term": "y",
            "submit": "Register"
        }

        response = self._request('post', 'reg', data=data)
        return response

    def login(self, username, password):
        data = {
            "username": username,
            "password": password,
            "submit": "Login"
        }

        return self._request('post', 'login', data=data)

    def get_session_cookie(self, username, password):
        data = {
            "username": username,
            "password": password,
            "submit": "Login"
        }
        return self.get_session('post', 'login', data=data)

    def delete_user(self, username):
        return self._request('delete', f'api/user/{username}')

    def change_password(self, username, new_password):
        data = {
            'password': new_password
        }
        res = self._request('put', f'api/user/{username}/change-password', json=data)
        return res

    def block_user(self, username):
        return self._request('post', f'api/user/{username}/block')

    def unblock_user(self, username):
        return self._request('post', f'api/user/{username}/accept')
