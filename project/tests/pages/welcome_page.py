from pages.base_page import BasePage
from locators.welcome_locators import WelcomeLocators


class WelcomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'http://myapp:1000/welcome/'
        self.locators = WelcomeLocators

    def click_logout_button(self):
        from pages.login_page import LoginPage
        self.click(self.locators.LOGOUT_BUTTON)
        return LoginPage(self.driver)

    def get_login_name_data(self):
        return self.get_element_html(self.locators.LOGIN_NAME)
