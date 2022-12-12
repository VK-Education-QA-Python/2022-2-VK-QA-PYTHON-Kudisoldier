from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from locators.base_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = None
        self.locators = None

    def click(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    def fill_input(self, locator, string_to_fill):
        input_filed = self.driver.find_element(*locator)
        input_filed.clear()
        input_filed.send_keys(string_to_fill)

    def wait_until_visible(self, locator):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_clickable(self, locator):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(locator)
        )

    def open_page(self, url):
        self.driver.get(url)

    def find(self, locator):
        try:
            element = self.driver.find_element(*locator)
        except NoSuchElementException:
            return 'not found'

        return element

    def wait_until_invisible(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located(locator)
        )

    def get_current_url(self):
        return self.driver.current_url

    def open(self):
        self.open_page(self.url)

    def driver_load_requests_session(self, requests_session):
        for cookie in requests_session.cookies:
            self.driver.add_cookie({
                'name': cookie.name,
                'path': cookie.path,
                'value': cookie.value
            })

    def check_page(self):
        return self.driver.current_url == self.url
