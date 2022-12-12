from selenium.webdriver.common.by import By


class BasePageLocators:
    POWERED_BY_TEXT = (By.XPATH, "//div[contains(@class, 'uk-text-center uk-text-large')]")
    ERROR_NOTIFICATION = (By.XPATH, "//div[contains(@id, 'flash')]")
