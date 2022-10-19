from selenium.webdriver.common.by import By
from locators.base_locators import BasePageLocators


class DashboardLocators(BasePageLocators):
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, "//div[contains(@class, 'dashboard-module-createButton')]")
    CAMPAIGN_ACTIONS = (By.XPATH, "//div[contains(@class, 'tableControls-module-massActionsSelect')]")
    CAMPAIGN_ACTIONS_DELETE = (By.XPATH, "//li[contains(@class, 'optionsList-module-option')"
                                         " and contains(@data-id, '8')]")
    SEGMENTS_BUTTON = (By.XPATH, "//a[contains(@class, 'center-module-segments')]")
    SUCCESS_NOTIFICATION = (By.XPATH, "//div[contains(@class, 'notify-module-success')]")
    SUCCESS_NOTIFICATION_CLOSE = (By.XPATH, "//div[contains(@class, 'notify-module-success')]//span")

    @staticmethod
    def get_campaign_locator(campaign_uuid):
        campaign_locator = (By.XPATH, f"//a[contains(@title, '{campaign_uuid}')]")
        return campaign_locator

    @staticmethod
    def get_campaign_checkbox_locator(campaign_uuid):
        campaign_checkbox_locator = (By.XPATH, f"//a[contains(@title, '{campaign_uuid}')]"
                                               f"/parent::div//input[contains(@class, 'nameCell-module')]")
        return campaign_checkbox_locator
