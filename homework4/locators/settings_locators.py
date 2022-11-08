from appium.webdriver.common.appiumby import AppiumBy


class SettingsLocators:
    NEWS_SOURCES = (AppiumBy.ID, "ru.mail.search.electroscope:id/user_settings_field_news_sources")
    ABOUT_BUTTON = (AppiumBy.ID, "ru.mail.search.electroscope:id/user_settings_about")
    SETTINGS_BUTTONS = (AppiumBy.XPATH, "//*[contains(@resource-id, 'ru.mail.search.electroscope:id/user_settings_')]")
    CLOSE_BUTTON = (AppiumBy.XPATH, '//android.widget.LinearLayout'
                                    '[@resource-id="ru.mail.search.electroscope:id/user_settings_toolbar"]'
                                    '/android.widget.ImageButton')
