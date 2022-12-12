from selenium.webdriver.common.by import By
from locators.base_locators import BasePageLocators


class WelcomeLocators(BasePageLocators):
    LOGOUT_BUTTON = (By.XPATH, "//div[contains(@id, 'logout')]")
