import time


def test_basic(dashboard_page):
    dashboard_page.wait_until_page_loaded()
    time.sleep(10)
