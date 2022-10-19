from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://target-sandbox.my.com/'

    def open_main_page(self):
        self.open_page(self.url)
        self.wait_until_page_loaded()

    def go_to_dashboard(self):
        from pages.dashboard_page import DashboardPage
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.open_dashboard_page()
        return dashboard_page
