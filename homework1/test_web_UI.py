import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import locators
from conftest import login_with_credentials, element_position_fixed
import string
import random


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
        element_position_fixed(locators.LOGOUT_BUTTON)
    )
    logout_button.click()

    assert session.current_url == 'https://target-sandbox.my.com/'


@pytest.mark.UI
@pytest.mark.negative
def test_login_wrong_credentials(driver):
    login_with_credentials(driver, 'abc@mail.ru', 'b')
    driver.find_element(*locators.WRONG_CREDENTIALS_ERROR)


@pytest.mark.UI
@pytest.mark.negative
def test_login_forbidden_credentials(driver):
    login_with_credentials(driver, 'a', 'b')
    driver.find_element(*locators.FORBIDDEN_CREDENTIALS_ERROR)


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

