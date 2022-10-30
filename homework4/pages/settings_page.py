from pages.base_page import BasePage
from locators.settings_locators import SettingsLocators


class SettingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SettingsLocators

    def open_news_source(self):
        from pages.news_source_page import NewsSourcePage
        settings_elements = self.find_elements(self.locators.SETTINGS_BUTTONS)
        settings_elements = [i for i in settings_elements if i.get_attribute('clickable') == 'true']

        menu_id = 'ru.mail.search.electroscope:id/user_settings_field_news_sources'
        while menu_id not in [i.get_attribute('resource-id') for i in settings_elements]:
            self.scroll_from_to(settings_elements[2], settings_elements[1])
            settings_elements = self.find_elements(self.locators.SETTINGS_BUTTONS)
            settings_elements = [i for i in settings_elements if i.get_attribute('clickable') == 'true']
        menu_index = [i.get_attribute('resource-id') for i in settings_elements].index(menu_id)
        settings_elements[menu_index].click()

        return NewsSourcePage(self.driver)

    def close(self):
        from pages.main_page import MainPage
        self.click(self.locators.CLOSE_BUTTON)

        return MainPage(self.driver)




