import pytest
import allure


@pytest.mark.UI
def test_campaign_create(dashboard_page):
    """
    advertising campaign test
    """
    with allure.step("Create new campaign"):
        new_campaign_page = dashboard_page.open_new_campaign_page()

        new_campaign_page.new_special_campaign()
        new_campaign_page.fill_campaign_url()
        new_campaign_page.wait_until_page_loaded()
        campaign_name = new_campaign_page.fill_campaign_name()
        new_campaign_page.scroll_campaign_creation()
        new_campaign_page.fill_campaign_text()
        dashboard_page = new_campaign_page.create_campaign()
        dashboard_page.wait_success_notification()

        dashboard_page.notification_close()

    with allure.step("Delete created campaign"):
        dashboard_page.find_campaign(campaign_name)
        dashboard_page.click_checkbox_campaign(campaign_name)
        dashboard_page.click_actions()
        dashboard_page.click_delete_action()
        dashboard_page.wait_success_notification()


@pytest.mark.UI
def test_segment_create(dashboard_page):
    """
    creation of segment with audience in app test
    """
    with allure.step("Create segment with audience in app"):
        segments_page = dashboard_page.open_segments_page()
        segments_page.open_segments_new_segment()

        segments_page.click_apps_and_games_segment()
        segments_page.click_played_checkbox()
        segments_page.click_add_segments_button()
        segment_name = segments_page.fill_segment_name()
        segments_page.click_create_segment_button()
        segments_page.find_segment(segment_name)

    with allure.step("Delete previosly created segment with audience in app"):
        segments_page.click_segment_checkbox(segment_name)
        segments_page.click_actions()
        segments_page.click_delete()
        segments_page.wait_success_notification()


@pytest.mark.UI
def test_segment_vk_group_create(dashboard_page):
    """
    creation of segment with vk edu group test
    """
    with allure.step("Create segment with vk edu group test"):
        segments_page = dashboard_page.open_segments_page()

        segments_page.click_ok_vk_datasource()
        segments_page.wait_until_page_loaded()

        segments_page.fill_group_input()
        segments_page.add_group()

        segments_page.open_segments_new_segment()
        segments_page.click_ok_and_vk_segment()
        segments_page.click_played_checkbox()
        segments_page.click_add_segments_button()
        segment_name = segments_page.fill_segment_name()
        segments_page.click_create_segment_button()
        segments_page.find_segment(segment_name)

    with allure.step("Delete segment with vk edu group test"):
        segments_page.click_segment_checkbox(segment_name)
        segments_page.click_actions()
        segments_page.click_delete()
        segments_page.wait_success_notification()

        segments_page.click_ok_vk_datasource()
        segments_page.click_vk_edu_remove()
