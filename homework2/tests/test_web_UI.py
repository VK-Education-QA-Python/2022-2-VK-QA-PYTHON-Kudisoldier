import time


def test_campaign_create(dashboard_page):
    new_campaign_page = dashboard_page.open_new_campaign_page()

    new_campaign_page.new_special_campaign()
    new_campaign_page.fill_campaign_url()
    new_campaign_page.wait_until_page_loaded()
    campaign_name = new_campaign_page.fill_campaign_name()
    new_campaign_page.scroll_campaign_creation()
    new_campaign_page.fill_campaign_text()
    dashboard_page = new_campaign_page.create_campaign()
    dashboard_page.find_campaign(campaign_name)

    dashboard_page.click_checkbox_campaign(campaign_name)
    dashboard_page.click_actions()
    dashboard_page.click_delete_action()


