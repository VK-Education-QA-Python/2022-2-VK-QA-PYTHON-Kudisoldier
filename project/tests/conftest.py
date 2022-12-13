import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.reg_page import RegistrationPage
from pages.welcome_page import WelcomePage
from database_client import DatabaseClient
from api.api_client import ApiClient
from api.mock_api_client import MockApiClient
from utils import generate_user_data
import allure


def pytest_addoption(parser):
    parser.addoption('--vnc', action='store_true')


@allure.title("Database client init")
@pytest.fixture()
def database_client(request):
    yield request.config.database_client
    request.config.database_client.session.close()


@allure.title("Api client init")
@pytest.fixture()
def client(request):
    database_client = request.config.database_client
    client = ApiClient()
    name, surname, username, email, password, middle_name,\
    access, active, start_active_time = generate_user_data()
    database_client.add_user(name, surname, middle_name, username,
                             password, email, access, active, start_active_time)
    client.login(username, password)
    yield client


@allure.title("Mock api client init")
@pytest.fixture()
def mock_client():
    mock_client = MockApiClient()
    yield mock_client


@pytest.fixture()
def config_params(request):
    vnc = request.config.getoption("--vnc")
    return {'vnc': vnc}


def pytest_configure(config):
    database_client = DatabaseClient('127.0.0.1', '3306', 'test_qa', 'qa_test', 'myappdb')
    database_client.connect()
    if not hasattr(config, 'workerinput'):
        database_client.truncate_table('test_users')
    config.database_client = database_client


@allure.title("Driver init")
@pytest.fixture
def driver(config_params):
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVideo": False,
            "enableVNC": config_params["vnc"]
        }
    }

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)

    yield driver
    driver.close()


@allure.title("Login page init")
@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.open()
    return login_page


@allure.title("Registration page init")
@pytest.fixture
def reg_page(driver):
    reg_page = RegistrationPage(driver)
    reg_page.open()
    return reg_page


@allure.title("Welcome page init")
@pytest.fixture
def welcome_page(driver):
    welcome_page = WelcomePage(driver)
    welcome_page.open()
    return welcome_page
