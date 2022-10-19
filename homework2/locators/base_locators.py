from selenium.webdriver.common.by import By


class BasePageLocators:
    SPINNER = (By.XPATH, "//div[contains(@class, 'spinner_large')]")