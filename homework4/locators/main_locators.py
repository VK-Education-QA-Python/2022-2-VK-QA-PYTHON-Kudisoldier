from appium.webdriver.common.appiumby import AppiumBy


class MainLocators:
    KEYBOARD_BUTTON = (AppiumBy.ID, "ru.mail.search.electroscope:id/keyboard")
    SEARCH_INPUT = (AppiumBy.ID, "ru.mail.search.electroscope:id/input_text")
    SEARCH_BUTTON = (AppiumBy.ID, "ru.mail.search.electroscope:id/text_input_send")
    SUGGESTED_ITEMS = (AppiumBy.ID, "ru.mail.search.electroscope:id/item_suggest_text")
    VOICE_ASSISTANT_BUTTON = (AppiumBy.ID, "ru.mail.search.electroscope:id/assistant_voice_input_group")
    FACT_CARD_TITLE = (AppiumBy.ID, "ru.mail.search.electroscope:id/item_dialog_fact_card_title")
