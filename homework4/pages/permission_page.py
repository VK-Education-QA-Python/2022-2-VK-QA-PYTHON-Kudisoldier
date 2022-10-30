from pages.base_page import BasePage
from locators.permission_locators import PermissionLocators
from pages.onboarding_page import OnboardingPage


class PermissionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PermissionLocators

    def allow_notifications(self):
        self.click(self.locators.ALLOW_BUTTON)

    def allow_location(self):
        self.click(self.locators.ALLOW_FOREGROUND_BUTTON)

    def allow_audio(self):
        self.click(self.locators.ALLOW_FOREGROUND_BUTTON)

    def allow_devices(self):
        self.click(self.locators.ALLOW_BUTTON)

    def allow_all(self):
        self.allow_notifications()
        self.allow_location()
        self.allow_audio()
        self.allow_devices()
        return OnboardingPage(self.driver)
