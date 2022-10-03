import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import locators


class element_position_fixed(object):
  """An expectation for checking that an element has a fixed position.

  locator - used to find the element
  returns the WebElement once it is not moving
  """
  def __init__(self, locator):
    self.locator = locator
    self.pos = None
    self.prev_pos = None

  def __call__(self, driver):
    element = driver.find_element(*self.locator)   # Finding the referenced element
    self.pos = element.rect
    if self.pos != self.prev_pos:   # Compare previous and current positions
        self.prev_pos = self.pos
        return False
    else:
        return element


def test_login(session):
    assert session.current_url == 'https://target-sandbox.my.com/dashboard'


def test_logout(session):
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
