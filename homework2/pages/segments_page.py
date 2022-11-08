import selenium.common.exceptions
from pages.base_page import BasePage
from locators.segments_locators import SegmentsLocators
import uuid


class SegmentsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://target-sandbox.my.com/segments/segments_list/'
        self.locators = SegmentsLocators

    def open_segments_new_segment(self):
        self.open_page(self.url + 'new/')
        self.wait_until_page_loaded()

    def click_apps_and_games_segment(self):
        self.wait_until_clickable(self.locators.APPS_AND_GAMES)
        self.click(self.locators.APPS_AND_GAMES)

    def click_played_checkbox(self):
        self.click(self.locators.PLAYED_CHECKBOX)

    def click_add_segments_button(self):
        self.click(self.locators.ADD_SEGMENTS_BUTTON)

    def fill_segment_name(self):
        segment_name = str(uuid.uuid4())
        self.fill_input(self.locators.SEGMENT_NAME_INPUT, segment_name)
        return segment_name

    def click_create_segment_button(self):
        self.click(self.locators.CREATE_SEGMENT_BUTTON)

    def find_segment(self, segment_uuid):
        try:
            self.wait_until_visible(self.locators.get_segment_locator(segment_uuid))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False


    def click_segment_checkbox(self, segment_uuid):
        href = self.find(self.locators.get_segment_href(segment_uuid)).get_attribute("href")
        segment_id = href.split('/')[-1]
        self.click(self.locators.get_segment_checkbox(segment_id))

    def click_actions(self):
        self.click(self.locators.SEGMENTS_ACTIONS)

    def click_delete(self):
        self.click(self.locators.DELETE_BUTTON)

    def wait_success_notification(self):
        try:
            self.wait_until_visible(self.locators.SUCCESS_NOTIFICATION)
            return True
        except selenium.common.exceptions.TimeoutException:
            return False

    def click_ok_vk_datasource(self):
        self.click(self.locators.OK_AND_VK_GROUP_DATASOURCE)

    def fill_group_input(self):
        self.fill_input(self.locators.GROUP_INPUT, 'https://vk.ru/vkedu')

    def add_group(self):
        self.wait_until_clickable(self.locators.SELECT_ALL)
        self.click(self.locators.SELECT_ALL)
        self.click(self.locators.ADD_SELECTED)

    def click_ok_and_vk_segment(self):
        self.wait_until_clickable(self.locators.GROUPS_OK_AND_VK)
        self.click(self.locators.GROUPS_OK_AND_VK)

    def click_vk_edu_remove(self):
        self.click(self.locators.CLOSE_BUTTON_VK_EDU_GROUP)
        self.click(self.locators.ACCEPT_REMOVE)
        self.wait_until_invisible(self.locators.ACCEPT_REMOVE)
        self.wait_until_invisible(self.locators.CLOSE_BUTTON_VK_EDU_GROUP)

