from api.base_api import BaseApi


class ApiClient(BaseApi):
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



