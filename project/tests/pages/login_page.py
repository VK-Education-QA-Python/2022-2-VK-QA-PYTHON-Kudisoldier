from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'http://myapp:1000/login'
        self.locators = LoginLocators

    def click_login_button(self):
        self.click(self.locators.LOGIN_BUTTON)
        result = self.find(self.locators.ERROR_NOTIFICATION)
        return result

    def login(self, username, password):
        self.fill_input(self.locators.USERNAME_INPUT, username)
        self.fill_input(self.locators.PASSWORD_INPUT, password)
        result = self.click_login_button()
        if result == 'not found':
            return 'success'
        else:
            return 'error'

    def go_to_registration(self):
        from pages.reg_page import RegistrationPage
        self.click(self.locators.GO_TO_REGISTRATION_BUTTON)
        return RegistrationPage(self.driver)
