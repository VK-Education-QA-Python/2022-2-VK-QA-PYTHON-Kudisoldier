from appium.webdriver.common.appiumby import AppiumBy


class PermissionLocators:
    ALLOW_BUTTON = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    ALLOW_FOREGROUND_BUTTON = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")

