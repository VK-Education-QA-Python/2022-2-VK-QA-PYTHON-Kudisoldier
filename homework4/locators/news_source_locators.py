from appium.webdriver.common.appiumby import AppiumBy


class NewsSourceLocators:
    NEWS_PROVIDERS = (AppiumBy.ID, "ru.mail.search.electroscope:id/news_sources_item_title")
    SELECTED_PROVIDER = (AppiumBy.XPATH, '//android.widget.ImageView'
                                         '[@resource-id="ru.mail.search.electroscope:id/news_sources_item_selected"]'
                                         '/parent::*/android.widget.TextView')
    CLOSE_BUTTON = (AppiumBy.XPATH, '//android.widget.LinearLayout'
                                    '[@resource-id="ru.mail.search.electroscope:id/news_sources_toolbar"]'
                                    '/android.widget.ImageButton')
