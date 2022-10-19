from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://target-sandbox.my.com/'
        self.open_main_page()

    def open_main_page(self):
        self.driver.get(self.url)
        self.wait_until_page_loaded()

    def go_to_dashboard(self):
        return DashboardPage(self.driver)
