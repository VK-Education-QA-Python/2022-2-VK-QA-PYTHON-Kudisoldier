from pages.base_page import BasePage
from locators.main_locators import MainLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainLocators

    def search_text(self, text):
        self.wait_until_visible(self.locators.VOICE_ASSISTANT_BUTTON)
        self.click(self.locators.KEYBOARD_BUTTON)
        self.fill_input(self.locators.SEARCH_INPUT, text)
        self.click(self.locators.SEARCH_BUTTON)

    def swipe_suggested(self, card_text):
        suggested_elements = self.find_elements(self.locators.SUGGESTED_ITEMS)
        while suggested_elements[-1].get_attribute('text') != card_text:
            self.scroll_from_to(suggested_elements[1], suggested_elements[0])
            suggested_elements = self.find_elements(self.locators.SUGGESTED_ITEMS)
        self.click(suggested_elements[-1])

    def get_fact_result(self):
        return self.find_element(self.locators.FACT_CARD_TITLE).get_attribute('text')

