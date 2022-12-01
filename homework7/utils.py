import time
import requests
import multiprocessing
from uvicorn import Config, Server
import logging


class NoParsingFilter(logging.Filter):
    def filter(self, record):
        return record.getMessage().find('Starting') == -1 and \
               record.getMessage().find('http://127.0.0.1:2000') != -1


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
