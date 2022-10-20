import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import utils
from api import api_client
from pages.main_page import MainPage
import allure


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')


@pytest.fixture()
def config(request):
    headless = request.config.getoption("--headless")
    if request.config.getoption('--selenoid'):
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
        selenoid = 'http://127.0.0.1:4444/wd/hub'
    else:
        selenoid = None
        vnc = False
    return {'headless': headless, 'vnc': vnc, 'selenoid': selenoid}


@allure.title("Driver setup")
@pytest.fixture()
def driver(config):
    options = Options()
    options.headless = config["headless"]
    if config['selenoid']:
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "91.0",
            "selenoid:options": {
                "enableVideo": False
            }
        }

        driver = webdriver.Remote(
            command_executor=config['selenoid'],
            desired_capabilities=capabilities)
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="105.0.5195.19").install()),
                                  options=options)
    driver.set_window_size(1280, 720)

    yield driver
    driver.close()


@allure.title("Dashboard page init")
@pytest.fixture()
def dashboard_page(driver):
    email, password = utils.get_credentials()
    requests_session = api_client.login(email, password)
    main_page = MainPage(driver)
    main_page.open_main_page()
    utils.driver_load_requests_session(driver, requests_session)
    dashboard_page = main_page.go_to_dashboard()

    yield dashboard_page

    res = ''
    for i in driver.get_log('browser'):
        res += f"{i['level']} - {i['source']}\n{i['message']}\n"
    allure.attach(res, name="browser log", attachment_type=allure.attachment_type.TEXT)


