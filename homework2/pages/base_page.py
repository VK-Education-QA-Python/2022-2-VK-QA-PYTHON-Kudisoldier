from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = None

    def wait_until_page_loaded(self):
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element(BasePageLocators.SPINNER)
        )

    def click(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    def fill_input(self, locator, string_to_fill):
        input_filed = self.driver.find_element(*locator)
        input_filed.clear()
        input_filed.send_keys(string_to_fill)
