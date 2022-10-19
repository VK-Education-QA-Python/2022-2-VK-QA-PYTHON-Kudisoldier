from pages.base_page import BasePage
from locators.new_campaign_locators import NewCampaignLocators
import uuid


class NewCampaignPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://target-sandbox.my.com/campaign/new'
        self.wait_until_page_loaded()

    def new_special_campaign(self):
        self.click(NewCampaignLocators.SPECIAL_CAMPAIGN)

    def fill_campaign_url(self):
        self.fill_input(NewCampaignLocators.CAMPAIGN_INPUT, "https://vk.ru/testers")

    def fill_campaign_name(self):
        campaign_name = str(uuid.uuid4())
        self.wait_until_visible(NewCampaignLocators.CAMPAIGN_NAME_INPUT)
        self.fill_input(NewCampaignLocators.CAMPAIGN_NAME_INPUT, campaign_name)
        return campaign_name

    def scroll_campaign_creation(self):
        self.click(NewCampaignLocators.CREATE_CAMPAIGN_STEP)

    def fill_campaign_text(self):
        self.wait_until_visible(NewCampaignLocators.CAMPAIGN_TEXT_INPUT)
        self.fill_input(NewCampaignLocators.CAMPAIGN_TEXT_INPUT, str(uuid.uuid4()))

    def create_campaign(self):
        from pages.dashboard_page import DashboardPage
        self.wait_until_visible(NewCampaignLocators.CREATE_CAMPAIGN_BUTTON)
        self.click(NewCampaignLocators.CREATE_CAMPAIGN_BUTTON)

        return DashboardPage(self.driver)
