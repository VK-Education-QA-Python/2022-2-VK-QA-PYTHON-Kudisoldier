from pages.base_page import BasePage
from locators.onboarding_locators import OnboardingLocators
from pages.main_page import MainPage


class OnboardingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OnboardingLocators

    def close_onboarding(self):
        self.click(self.locators.CLOSE_BUTTON)
        return MainPage(self.driver)
