from pages.base_page import BasePage
from locators.settings_locators import SettingsLocators


class SettingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SettingsLocators

    def scroll_to_item_menu_and_click(self, menu_id):
        settings_elements = self.find_elements(self.locators.SETTINGS_BUTTONS)
        settings_elements = [i for i in settings_elements if i.get_attribute('clickable') == 'true']

        while menu_id not in [i.get_attribute('resource-id') for i in settings_elements]:
            self.scroll_from_to(settings_elements[2], settings_elements[1])
            settings_elements = self.find_elements(self.locators.SETTINGS_BUTTONS)
            settings_elements = [i for i in settings_elements if i.get_attribute('clickable') == 'true']
        menu_index = [i.get_attribute('resource-id') for i in settings_elements].index(menu_id)
        self.click(settings_elements[menu_index])

    def open_news_source(self):
        from pages.news_source_page import NewsSourcePage
        menu_id = self.locators.NEWS_SOURCES[1]
        self.scroll_to_item_menu_and_click(menu_id)
        return NewsSourcePage(self.driver)

    def close(self):
        from pages.main_page import MainPage
        self.click(self.locators.CLOSE_BUTTON)

        return MainPage(self.driver)

    def open_about(self):
        from pages.about_page import AboutPage

        menu_id = self.locators.ABOUT_BUTTON[1]
        self.scroll_to_item_menu_and_click(menu_id)

        return AboutPage(self.driver)
