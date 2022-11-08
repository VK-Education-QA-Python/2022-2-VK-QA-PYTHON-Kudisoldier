from appium.webdriver.common.appiumby import AppiumBy


class AboutLocators:
    APP_VERSION = (AppiumBy.ID, "ru.mail.search.electroscope:id/about_version")
    APP_COPYRIGHT = (AppiumBy.ID, "ru.mail.search.electroscope:id/about_copyright")
