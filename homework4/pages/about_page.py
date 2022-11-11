from pages.base_page import BasePage
from locators.about_locators import AboutLocators


class AboutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AboutLocators

    def get_app_version(self):
        return self.find_element(self.locators.APP_VERSION).get_attribute('text')

    def get_app_copyright(self):
        return self.find_element(self.locators.APP_COPYRIGHT).get_attribute('text')
