import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import utils
from api import api_client
from pages.main_page import MainPage


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
def dashboard_page(driver):
    email, password = utils.get_credentials()
    requests_session = api_client.login(email, password)
    main_page = MainPage(driver)
    utils.driver_load_requests_session(driver, requests_session)
    dashboard_page = main_page.go_to_dashboard()

    return dashboard_page
