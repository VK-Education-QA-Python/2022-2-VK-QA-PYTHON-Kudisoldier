import pytest
import multiprocessing
from uvicorn import Config, Server
import time
import requests
import settings


class UvicornServer(multiprocessing.Process):

    def __init__(self, config: Config):
        super().__init__()
        self.server = Server(config=config)
        self.config = config

    def stop(self):
        self.terminate()

    def run(self, *args, **kwargs):
        self.server.run()


def wait_ready(host, port):
    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{host}:{port}/')
            started = True
            break
        except requests.exceptions.ConnectionError:
            pass

    if not started:
        raise RuntimeError('App did not started in 5s!')


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        server_config = Config("application.app:app", host=settings.APP_HOST,
                               port=settings.APP_PORT, log_level="debug")
        config.instance_app = UvicornServer(config=server_config)
        config.instance_app.start()
        wait_ready(settings.APP_HOST, settings.APP_PORT)

        stub_server_config = Config("stub.fastapi_stub:app", host=settings.STUB_HOST,
                               port=settings.STUB_PORT, log_level="debug")
        config.instance_stub = UvicornServer(config=stub_server_config)
        config.instance_stub.start()
        wait_ready(settings.STUB_HOST, settings.STUB_PORT)

        mock_server_config = Config("mock.fastapi_mock:app", host=settings.MOCK_HOST,
                               port=settings.MOCK_PORT, log_level="debug")
        config.instance_mock = UvicornServer(config=mock_server_config)
        config.instance_mock.start()
        wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)


def pytest_unconfigure(config):
    config.instance_app.stop()
    config.instance_stub.stop()
    config.instance_mock.stop()
