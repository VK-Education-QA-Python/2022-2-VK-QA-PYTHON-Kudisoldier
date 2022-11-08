from selenium.webdriver.common.by import By
from locators.base_locators import BasePageLocators


class NewCampaignLocators(BasePageLocators):
    SPECIAL_CAMPAIGN = (By.XPATH, "//div[contains(@class, 'column-list-item _special')]")
    CAMPAIGN_INPUT = (By.XPATH, "//input[contains(@class, 'mainUrl-module-searchInput')]")
    CAMPAIGN_NAME_INPUT = (By.XPATH, "//div[contains(@class, 'input_campaign-name')]//input")
    CREATE_CAMPAIGN_STEP = (By.XPATH, "//li[contains(@class, 'js-progress-item-banners')]")
    CAMPAIGN_TEXT_INPUT = (By.XPATH, "//input[contains(@data-gtm-id, 'banner_form_text')]")
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, "//div[contains(@class, 'js-save-button-wrap')]")
