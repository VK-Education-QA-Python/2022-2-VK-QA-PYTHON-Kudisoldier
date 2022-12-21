from selenium.webdriver.common.by import By
from locators.base_locators import BasePageLocators


class LoginLocators(BasePageLocators):
    LOGIN_BUTTON = (By.XPATH, "//input[contains(@value, 'Login')]")
    USERNAME_INPUT = (By.XPATH, "//input[contains(@id, 'username')]")
    PASSWORD_INPUT = (By.XPATH, "//input[contains(@id, 'password')]")
    GO_TO_REGISTRATION_BUTTON = (By.XPATH, "//a[contains(@href, '/reg')]")
