from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://target-sandbox.my.com/dashboard'
        self.open_dashboard_page()

    def open_dashboard_page(self):
        self.driver.get(self.url)
        self.wait_until_page_loaded()
