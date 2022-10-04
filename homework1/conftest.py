import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import locators
from selenium.webdriver.chrome.options import Options


LOGIN = '2jorzjylbglw@mail.ru'
PASSWORD = '2jorzjylbglw'


class element_position_fixed(object):
  """An expectation for checking that an element has a fixed position.

  locator - used to find the element
  retries - used to define how many retries element should not move
  returns the WebElement once it is not moving
  """
  def __init__(self, locator):
    self.locator = locator
    self.prev_pos = None

  def __call__(self, driver):
    element = driver.find_element(*self.locator)   # Finding the referenced element
    pos = element.rect

    if pos != self.prev_pos:   # Compare previous and current positions
        self.prev_pos = pos
        return False
    else:  # pos == prev_pos and counter >= retries
        return element


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
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.fixture()
def session(driver):
    login_with_credentials(driver, LOGIN, PASSWORD)
    yield driver
