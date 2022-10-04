import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import locators
import string
import random


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


@pytest.mark.UI
@pytest.mark.positive
def test_login(session):
    assert session.current_url == 'https://target-sandbox.my.com/dashboard'


@pytest.mark.UI
@pytest.mark.positive
def test_logout(session):
    # wait until whole page loaded
    WebDriverWait(session, 30).until(
        EC.presence_of_element_located(locators.GETTING_STARTED_TITLE)
    )

    account = WebDriverWait(session, 30).until(
        EC.element_to_be_clickable(locators.ACCOUNT_BUTTON)
    )
    account.click()

    # set low poll_frequency to detect animation
    logout_button = WebDriverWait(session, 30, poll_frequency=0.05).until(
        element_position_fixed(locators.LOGOUT_BUTTON)  # use custom wait class
    )
    logout_button.click()

    assert session.current_url == 'https://target-sandbox.my.com/'


@pytest.mark.UI
@pytest.mark.negative
@pytest.mark.session_login('abc@mail.ru')
@pytest.mark.session_password('b')
def test_login_wrong_credentials(session):
    session.find_element(*locators.WRONG_CREDENTIALS_ERROR)


@pytest.mark.UI
@pytest.mark.negative
@pytest.mark.session_login('a')
@pytest.mark.session_password('b')
def test_login_forbidden_credentials(session):
    session.find_element(*locators.FORBIDDEN_CREDENTIALS_ERROR)


@pytest.mark.UI
@pytest.mark.positive
def test_change_contacts(session):
    session.get('https://target-sandbox.my.com/profile/contacts')

    name_input = WebDriverWait(session, 30).until(
        EC.presence_of_element_located(locators.NAME_INPUT)
    )
    name_input.clear()
    name_input.send_keys(''.join(random.choices(string.ascii_lowercase, k=5)))

    inn_input = session.find_element(*locators.INN_INPUT)
    inn_input.clear()
    inn_input.send_keys(''.join(random.choices(string.digits, k=12)))

    phone_input = session.find_element(*locators.PHONE_INPUT)
    phone_input.clear()
    phone_input.send_keys('+7' + ''.join(random.choices(string.digits, k=10)))

    submit_button = session.find_element(*locators.SUBMIT_BUTTON)
    submit_button.click()

    WebDriverWait(session, 30).until(
        EC.visibility_of_element_located(locators.SUCCESS_NOTIFICATION)
    )


@pytest.mark.UI
@pytest.mark.positive
@pytest.mark.parametrize("input_button,expected_element", [
                        (locators.SEGMENTS_BUTTON, locators.GETTING_STARTED_TITLE),
                        (locators.BALANCE_BUTTON, locators.DEPOSIT_BUTTON)
])
def test_page_navigation(input_button, expected_element, session):
    button = WebDriverWait(session, 30).until(
        EC.element_to_be_clickable(input_button)
    )
    button.click()

    WebDriverWait(session, 30).until(
        EC.visibility_of_element_located(expected_element)
    )
