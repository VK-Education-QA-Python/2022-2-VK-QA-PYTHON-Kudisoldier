import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import locators


LOGIN = '2jorzjylbglw@mail.ru'
PASSWORD = '2jorzjylbglw'


def login_with_credentials(driver, login, password):
    driver.get('https://target-sandbox.my.com')
    login_form_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(locators.LOGIN_FORM_BUTTON)
    )
    login_form_button.click()

    login_input = driver.find_element(*locators.LOGIN_INPUT)
    login_input.clear()
    login_input.send_keys(login)

    password_input = driver.find_element(*locators.PASSWORD_INPUT)
    password_input.clear()
    password_input.send_keys(password)

    login_button = driver.find_element(*locators.LOGIN_BUTTON)
    login_button.click()


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
def session(request, driver, login=LOGIN, password=PASSWORD):
    login_marker = request.node.get_closest_marker("session_login")
    password_marker = request.node.get_closest_marker("session_password")
    if login_marker is not None and password_marker is not None:
        login = login_marker.args[0]
        password = password_marker.args[0]

    login_with_credentials(driver, login, password)
    yield driver
