import os
import signal
import subprocess
import time
from copy import copy
import requests
import settings
import threading

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))


def wait_ready(host, port):
    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError('App did not started in 5s!')


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        # app configuration

        app_path = os.path.join(repo_root, 'application', 'app.py')

        env = copy(os.environ)
        env.update({'APP_HOST': settings.APP_HOST, 'APP_PORT': settings.APP_PORT})
        env.update({'STUB_HOST': settings.STUB_HOST, 'STUB_PORT': settings.STUB_PORT})
        env.update({'MOCK_HOST': settings.MOCK_HOST, 'MOCK_PORT': settings.MOCK_PORT})

        app_stderr = open('/tmp/app_stderr', 'w')
        app_stdout = open('/tmp/app_stdout', 'w')
        from application import app
        app.run_app()
        #app_proc = subprocess.Popen(['/Users/efim/PycharmProjects/2022-2-VK-QA-PYTHON-Kudisoldier/venv/bin/python3', app_path], stderr=app_stderr, stdout=app_stdout, env=env)

        #config.app_proc = app_proc
        config.app_stderr = app_stderr
        config.app_stdout = app_stdout
        #time.sleep(200)
        wait_ready(settings.APP_HOST, settings.APP_PORT)

        ######### stub configuration #########

        stub_path = os.path.join(repo_root, 'stub', 'flask_stub.py')

        stub_stderr = open('/tmp/stub_stderr', 'w')
        stub_stdout = open('/tmp/stub_stdout', 'w')
        from stub import flask_stub
        flask_stub.run_stub()
        #config.stub_proc = stub_proc
        config.stub_stderr = stub_stderr
        config.stub_stdout = stub_stdout
        wait_ready(settings.STUB_HOST, settings.STUB_PORT)

        ######### mock configuration #########

        from mock import flask_mock
        flask_mock.run_mock()

        wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)


def pytest_unconfigure(config):
    pass
    # config.app_proc.terminate()
    # exit_code = config.app_proc.wait()
    #
    # config.app_stderr.close()
    # config.app_stdout.close()
    #
    # assert exit_code == 1
    #
    # config.stub_proc.terminate()
    # exit_code = config.stub_proc.wait()
    #
    # config.stub_stderr.close()
    # config.stub_stdout.close()
    #
    # assert exit_code == 1
    #
    # # TODO: add mock shutdown
    # requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')

