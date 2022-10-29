import pytest
from api.api_client import ApiClient
import utils


@pytest.fixture()
def client():
    email, password = utils.get_credentials()

    client = ApiClient()
    client.login(email, password)

    yield client


