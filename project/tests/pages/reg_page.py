from pages.base_page import BasePage
from locators.reg_locators import RegistrationLocators


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'http://myapp:1000/reg'
        self.locators = RegistrationLocators

    def click_register_button(self):
        self.click(self.locators.REGISTER_BUTTON)
        result = self.find(self.locators.ERROR_NOTIFICATION)
        return result

    def register(self, name, surname, middle_name, username, email, password):
        self.fill_input(self.locators.USER_NAME_INPUT, name)
        self.fill_input(self.locators.USER_SURNAME_INPUT, surname)
        self.fill_input(self.locators.USER_MIDDLE_NAME_INPUT, middle_name)
        self.fill_input(self.locators.USERNAME_INPUT, username)
        self.fill_input(self.locators.EMAIL_INPUT, email)
        self.fill_input(self.locators.PASSWORD_INPUT, password)
        self.fill_input(self.locators.PASSWORD_CONFIRM_INPUT, password)
        result = self.click_register_button()
        if result == 'not found':
            return 'success'
        else:
            return 'error'
