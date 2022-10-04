import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import locators
from conftest import login_with_credentials, element_position_fixed


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
