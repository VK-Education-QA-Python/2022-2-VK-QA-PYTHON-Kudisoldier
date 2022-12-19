from uvicorn import Config
import settings
import logging
import utils
import pytest
from api.app_client import AppApiClient
from api.mock_client import MockApiClient
from api.stub_client import StubApiClient


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        server_config = Config("application.app:app", host=settings.APP_HOST,
                               port=int(settings.APP_PORT))
        config.instance_app = utils.UvicornServer(config=server_config)
        config.instance_app.start()

        utils.wait_ready(settings.APP_HOST, settings.APP_PORT)

        stub_server_config = Config("stub.fastapi_stub:app", host=settings.STUB_HOST,
                                    port=int(settings.STUB_PORT))
        config.instance_stub = utils.UvicornServer(config=stub_server_config)
        config.instance_stub.start()
        utils.wait_ready(settings.STUB_HOST, settings.STUB_PORT)

        log = logging.getLogger('urllib3.connectionpool')
        log.addFilter(utils.NoParsingFilter())
        logging.basicConfig(filename='homework7/mock.log',
                            filemode='w',
                            level=logging.DEBUG,
                            format='%(asctime)s %(message)s')

        mock_server_config = Config("mock.fastapi_mock:app", host=settings.MOCK_HOST,
                                    port=int(settings.MOCK_PORT))
        config.instance_mock = utils.UvicornServer(config=mock_server_config)
        config.instance_mock.start()
        utils.wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)


def pytest_unconfigure(config):
    config.instance_app.stop()
    config.instance_stub.stop()
    config.instance_mock.stop()


@pytest.fixture(scope="session")
def app_client():
    client = AppApiClient()
    return client


@pytest.fixture(scope="session")
def mock_client():
    client = MockApiClient()
    return client


@pytest.fixture(scope="session")
def stub_client():
    client = StubApiClient()
    return client
