from pages.base_page import BasePage
from locators.main_locators import MainLocators
from pages.settings_page import SettingsPage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainLocators

    def wait_controls(self):
        self.wait_until_visible(self.locators.VOICE_ASSISTANT_BUTTON)

    def search_text(self, text):
        self.wait_controls()
        self.click(self.locators.KEYBOARD_BUTTON)
        self.fill_input(self.locators.SEARCH_INPUT, text)
        self.click(self.locators.SEARCH_BUTTON)

    def swipe_suggested(self, card_text):
        suggested_elements = self.find_elements(self.locators.SUGGESTED_ITEMS)

        while card_text not in [i.get_attribute('text') for i in suggested_elements]:
            self.scroll_from_to(suggested_elements[1], suggested_elements[0])
            suggested_elements = self.find_elements(self.locators.SUGGESTED_ITEMS)
        found_element_index = [i.get_attribute('text') for i in suggested_elements].index(card_text)
        self.click(suggested_elements[found_element_index])

    def get_fact_result(self):
        return self.find_element(self.locators.FACT_CARD_TITLE).get_attribute('text')

    def get_chat_result(self):
        return self.find_elements(self.locators.CHAT_MESSAGE)[-1].get_attribute('text')

    def open_settings(self):
        self.wait_controls()
        self.click(self.locators.SETTINGS_BUTTON)
        return SettingsPage(self.driver)

    def get_audio_name(self):
        self.click(self.locators.REV_BUTTON)
        self.click(self.locators.PLAY_BUTTON)
        return self.find_element(self.locators.AUDIO_TRACK).get_attribute('text')
