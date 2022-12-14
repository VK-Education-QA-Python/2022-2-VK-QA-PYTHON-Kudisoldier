import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from login import login


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true')


@pytest.fixture()
def config(request):
    headless = request.config.getoption("--headless")
    return {"headless": headless}


@pytest.fixture()
def driver(config):
    options = Options()
    options.headless = config["headless"]

    driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="105.0.5195.19").install()),
                              options=options)
    driver.set_window_size(1024, 768)

    yield driver
    driver.close()


@pytest.fixture()
def session(request, driver):
    login_marker = request.node.get_closest_marker("session_login")
    password_marker = request.node.get_closest_marker("session_password")

    if login_marker is not None and password_marker is not None:
        username = login_marker.args[0]
        password = password_marker.args[0]
        login(driver, username, password)
    else:
        login(driver)

    yield driver
