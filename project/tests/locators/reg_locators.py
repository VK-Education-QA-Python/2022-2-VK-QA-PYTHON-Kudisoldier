from selenium.webdriver.common.by import By
from locators.base_locators import BasePageLocators


class RegistrationLocators(BasePageLocators):
    REGISTER_BUTTON = (By.XPATH, "//input[contains(@value, 'Register')]")
    USER_NAME_INPUT = (By.XPATH, "//input[contains(@id, 'user_name')]")
    USER_SURNAME_INPUT = (By.XPATH, "//input[contains(@id, 'user_surname')]")
    USER_MIDDLE_NAME_INPUT = (By.XPATH, "//input[contains(@id, 'user_middle_name')]")
    USERNAME_INPUT = (By.XPATH, "//input[contains(@id, 'username')]")
    EMAIL_INPUT = (By.XPATH, "//input[contains(@id, 'email')]")
    PASSWORD_INPUT = (By.XPATH, "//input[contains(@id, 'password')]")
    PASSWORD_CONFIRM_INPUT = (By.XPATH, "//input[contains(@id, 'confirm')]")
    RULES_CONFIRM_CHECKBOX = (By.XPATH, "//input[contains(@id, 'term')]")
