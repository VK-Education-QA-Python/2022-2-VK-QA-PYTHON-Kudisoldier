import pytest
import string
import random
from base import *


@pytest.mark.UI
@pytest.mark.positive
def test_login(session):
    wait_until_page_loaded(session)
    session.find_element(*locators.ACCOUNT_BUTTON)


@pytest.mark.UI
@pytest.mark.positive
def test_logout(session):
    wait_until_page_loaded(session)

    click(session, locators.ACCOUNT_BUTTON)
    click_when_animation_ends(session, locators.LOGOUT_BUTTON)

    wait_until_page_loaded(session)
    session.find_element(*locators.LOGIN_FORM_BUTTON)


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

    wait_until_page_loaded(session)

    random_name = ''.join(random.choices(string.ascii_lowercase, k=5))
    fill_input(session, locators.NAME_INPUT, random_name)

    random_inn = ''.join(random.choices(string.digits, k=12))
    fill_input(session, locators.INN_INPUT, random_inn)

    random_phone = '+7' + ''.join(random.choices(string.digits, k=10))
    fill_input(session, locators.PHONE_INPUT, random_phone)

    click(session, locators.SUBMIT_BUTTON)

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
    wait_until_page_loaded(session)
    click(session, input_button)

    wait_until_page_loaded(session)
    WebDriverWait(session, 30).until(
        EC.visibility_of_element_located(expected_element)
    )
