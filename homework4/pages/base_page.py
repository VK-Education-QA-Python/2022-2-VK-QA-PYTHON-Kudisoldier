from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = None

    def click(self, locator):
        button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(locator)
        )
        button.click()

    def fill_input(self, locator, string_to_fill):
        input_filed = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        )
        input_filed.clear()
        input_filed.send_keys(string_to_fill)

    def find_elements(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        )
        elements = self.driver.find_elements(*locator)

        return elements

    def find_element(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        )
        element = self.driver.find_element(*locator)

        return element

    def scroll_from_to(self, element_from, element_to):
        actions = ActionChains(self.driver)
        actions.click_and_hold(element_from).move_to_element(element_to).release().perform()

    def wait_until_visible(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        )



