from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://target-sandbox.my.com/dashboard'

    def open_dashboard_page(self):
        self.driver.get(self.url)
        self.wait_until_page_loaded()

    def open_new_campaign_page(self):
        from pages.new_campaign_page import NewCampaignPage
        self.click(DashboardLocators.CREATE_CAMPAIGN_BUTTON)
        return NewCampaignPage(self.driver)

    def find_campaign(self, uuid):
        self.wait_until_visible(DashboardLocators.get_campaign_locator(uuid))

    def click_checkbox_campaign(self, uuid):
        self.click(DashboardLocators.get_campaign_checkbox_locator(uuid))

    def click_actions(self):
        self.wait_until_clickable(DashboardLocators.CAMPAIGN_ACTIONS)
        self.click(DashboardLocators.CAMPAIGN_ACTIONS)

    def click_delete_action(self):
        self.wait_until_clickable(DashboardLocators.CAMPAIGN_ACTIONS_DELETE)
        self.click(DashboardLocators.CAMPAIGN_ACTIONS_DELETE)
