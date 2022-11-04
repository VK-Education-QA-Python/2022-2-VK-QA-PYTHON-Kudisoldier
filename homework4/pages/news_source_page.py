from pages.base_page import BasePage
from locators.news_source_locators import NewsSourceLocators


class NewsSourcePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = NewsSourceLocators

    def choice_news_provider(self, news_provider_name):
        news_provider_elements = self.find_elements(self.locators.NEWS_PROVIDERS)
        chosen_news_provider_element = [i for i in news_provider_elements
                                        if i.get_attribute('text') == news_provider_name]
        chosen_news_provider_element[0].click()

    def get_selected_provider(self):
        return self.find_element(self.locators.SELECTED_PROVIDER).get_attribute('text')

    def close(self):
        from pages.settings_page import SettingsPage
        self.click(self.locators.CLOSE_BUTTON)

        return SettingsPage(self.driver)
