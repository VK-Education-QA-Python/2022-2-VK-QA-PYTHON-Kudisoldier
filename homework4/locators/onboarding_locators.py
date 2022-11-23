from appium.webdriver.common.appiumby import AppiumBy


class OnboardingLocators:
    CLOSE_BUTTON = (AppiumBy.XPATH,
                    "//android.widget.LinearLayout[@resource-id='ru.mail.search.electroscope:id/onboarding_toolbar']"
                    "/android.widget.ImageButton")
