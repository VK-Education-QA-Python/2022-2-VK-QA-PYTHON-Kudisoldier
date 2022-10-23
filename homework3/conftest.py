import pytest
from api.api import ApiClient


@pytest.fixture()
def client():
    email = '2jorzjylbglw@mail.ru'
    password = '2jorzjylbglw'

    client = ApiClient()
    client.login(email, password)

    yield client


