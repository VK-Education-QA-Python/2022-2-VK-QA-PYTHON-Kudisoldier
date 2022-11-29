#!/Users/efim/PycharmProjects/2022-2-VK-QA-PYTHON-Kudisoldier/venv/bin python3

import os
import random
from flask import Flask, jsonify
import threading
import settings

app = Flask(__name__)


@app.route('/get_age/<name>', methods=['GET'])
def get_user_age(name):
    return jsonify(random.randint(18, 105)), 200


@app.route('/me', methods=['GET'])
def stub():
    return 'stub'


def run_stub():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.STUB_HOST,
        'port': settings.STUB_PORT
    })

    server.start()
    return server
