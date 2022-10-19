from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = None
        self.locators = None

    def wait_until_page_loaded(self):
        WebDriverWait(self.driver, 120).until(
            EC.invisibility_of_element(BasePageLocators.SPINNER)
        )

    def click(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    def fill_input(self, locator, string_to_fill):
        input_filed = self.driver.find_element(*locator)
        input_filed.clear()
        input_filed.send_keys(string_to_fill)

    def wait_until_visible(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_clickable(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(locator)
        )

    def open_page(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def wait_until_page_changed(self, url):
        WebDriverWait(self.driver, 240).until(
            EC.url_changes(url)
        )

    def wait_until_invisible(self, locator):
        WebDriverWait(self.driver, 240).until(
            EC.invisibility_of_element_located(locator)
        )
