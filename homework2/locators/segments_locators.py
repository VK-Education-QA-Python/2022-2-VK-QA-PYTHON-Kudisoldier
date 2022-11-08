from selenium.webdriver.common.by import By
from locators.base_locators import BasePageLocators


class SegmentsLocators(BasePageLocators):
    APPS_AND_GAMES = (By.XPATH, "//div[contains(@class, 'adding-segments-item') and "
                                "contains(text(),'Приложения и игры в соцсетях')]")
    PLAYED_CHECKBOX = (By.XPATH, "//input[contains(@class, 'adding-segments-source')]")
    ADD_SEGMENTS_BUTTON = (By.XPATH, "//div[contains(@class, 'js-add-button')]")
    SEGMENT_NAME_INPUT = (By.XPATH, "//div[contains(@class, 'input_create-segment-form')]"
                                    "//input[contains(@class, 'js-form-element')]")
    CREATE_SEGMENT_BUTTON = (By.XPATH, "//div[contains(@class, 'create-segment-form__btn-wrap')]//button")
    SEGMENTS_ACTIONS = (By.XPATH, "//div[contains(@data-test, 'select')]//div[contains(@class, 'ctItem')]")
    DELETE_BUTTON = (By.XPATH, "//li[contains(@data-test, 'remove')]")
    SUCCESS_NOTIFICATION = (By.XPATH, "//div[contains(@class, 'notify-module-success')]")
    OK_AND_VK_GROUP_DATASOURCE = (By.XPATH, "//span[contains(@class, 'left-nav__text') and "
                                            "contains(text(),'Группы ОК и VK')]")
    GROUP_INPUT = (By.XPATH, "//div[contains(@class, 'multiSelectSuggester-module-wrapper')]//input")
    SELECT_ALL = (By.XPATH, "//div[contains(@data-test, 'select_all')]")
    ADD_SELECTED = (By.XPATH, "//div[contains(@data-test, 'add_selected_items_button')]")
    GROUPS_OK_AND_VK = (By.XPATH, "//div[contains(@class, 'adding-segments-item') and "
                                  "contains(text(),'Группы ОК и VK')]")
    CLOSE_BUTTON_VK_EDU_GROUP = (By.XPATH, "//a[@href='https://vk.com/vkedu']"
                                           "/parent::td/parent::tr//td[@data-id='remove']")
    ACCEPT_REMOVE = (By.XPATH, "//button[contains(@class, 'button_confirm-remove')]")

    @staticmethod
    def get_segment_locator(segment_uuid):
        segment_locator = (By.XPATH, f"//a[contains(@title, '{segment_uuid}')]")
        return segment_locator

    @staticmethod
    def get_segment_href(segment_uuid):
        campaign_href = (By.XPATH, f"//a[contains(@title, '{segment_uuid}')]")
        return campaign_href

    @staticmethod
    def get_segment_checkbox(segment_id):
        segment_checkbox = (By.XPATH, f"//div[contains(@class, 'main-module-CellFirst') and "
                                      f"contains(@data-test, '{segment_id}')]//input")
        return segment_checkbox
