from selenium.webdriver.common.by import By
from locators.base_locators import BasePageLocators


class DashboardLocators(BasePageLocators):
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, "//div[contains(@class, 'dashboard-module-createButton')]")
    CAMPAIGN_ACTIONS = (By.XPATH, "//div[contains(@class, 'tableControls-module-massActionsSelect')]")
    CAMPAIGN_ACTIONS_DELETE = (By.XPATH, "//li[contains(@class, 'optionsList-module-option')"
                                         " and contains(@data-id, '8')]")

    @staticmethod
    def get_campaign_locator(uuid):
        return (By.XPATH, f"//a[contains(@title, '{uuid}')]")

    @staticmethod
    def get_campaign_checkbox_locator(uuid):
        return (By.XPATH, f"//a[contains(@title, '{uuid}')]/parent::div//input[contains(@class, 'nameCell-module')]")
