from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import locators


class element_position_fixed(object):
  """An expectation for checking that an element has a fixed position.

  locator - used to find the element
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
    else:
        return element


def wait_until_page_loaded(driver):
    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element(locators.SPINNER)
    )


def click(driver, locator):
    button = driver.find_element(*locator)
    button.click()


def fill_input(driver, locator, string_to_fill):
    input_filed = driver.find_element(*locator)
    input_filed.clear()
    input_filed.send_keys(string_to_fill)


def click_when_animation_ends(driver, locator):
    # set low poll_frequency to detect animation
    button = WebDriverWait(driver, 30, poll_frequency=0.05).until(
        element_position_fixed(locator)  # use custom wait class
    )
    button.click()
