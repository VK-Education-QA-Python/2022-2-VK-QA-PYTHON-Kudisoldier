from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://target-sandbox.my.com/dashboard'
        self.locators = DashboardLocators

    def open_dashboard_page(self):
        self.open_page(self.url)
        self.wait_until_page_loaded()

    def open_new_campaign_page(self):
        from pages.new_campaign_page import NewCampaignPage
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON)
        self.wait_until_page_changed(self.url + '/new')
        self.wait_until_page_loaded()
        return NewCampaignPage(self.driver)

    def find_campaign(self, campaign_uuid):
        self.wait_until_visible(self.locators.get_campaign_locator(campaign_uuid))

    def click_checkbox_campaign(self, campaign_uuid):
        self.click(self.locators.get_campaign_checkbox_locator(campaign_uuid))

    def click_actions(self):
        self.wait_until_clickable(self.locators.CAMPAIGN_ACTIONS)
        self.click(self.locators.CAMPAIGN_ACTIONS)

    def click_delete_action(self):
        self.wait_until_clickable(self.locators.CAMPAIGN_ACTIONS_DELETE)
        self.click(self.locators.CAMPAIGN_ACTIONS_DELETE)

    def open_segments_page(self):
        from pages.segments_page import SegmentsPage
        self.click(self.locators.SEGMENTS_BUTTON)
        self.wait_until_page_loaded()
        return SegmentsPage(self.driver)

    def wait_success_notification(self):
        self.wait_until_visible(self.locators.SUCCESS_NOTIFICATION)

    def notification_close(self):
        self.click(self.locators.SUCCESS_NOTIFICATION_CLOSE)

