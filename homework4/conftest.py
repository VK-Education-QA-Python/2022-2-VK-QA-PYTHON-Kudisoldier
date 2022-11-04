import pytest
from appium import webdriver
import os
from pages.onboarding_page import OnboardingPage
from pages.main_page import MainPage
from selenium.common.exceptions import TimeoutException


@pytest.fixture()
def repo_root():
    return os.path.abspath(os.getcwd())


@pytest.fixture()
def driver(repo_root):
    caps = {}
    caps["appium:platformName"] = "android"
    caps["appium:appPackage"] = "ru.mail.search.electroscope"
    caps["appium:appActivity"] = "ru.mail.search.electroscope.ui.activity.AssistantActivity"
    caps["appium:app"] = repo_root + "/homework4/apk/marussia_1.70.0.apk"
    caps["appium:deviceName"] = "emulator-5554"
    caps["appium:newCommandTimeout"] = 3600
    caps["appium:autoGrantPermissions"] = True

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    yield driver

    driver.quit()


@pytest.fixture()
def main_page(driver):
    try:  # A/B test??
        onboarding_page = OnboardingPage(driver)
        main_page = onboarding_page.close_onboarding()
    except TimeoutException:
        main_page = MainPage(driver)

    return main_page


@pytest.fixture()
def version(repo_root):
    version_parsed = os.listdir(repo_root+'/homework4/apk')[0].replace('.apk', '').replace('marussia_', 'Версия ')
    return version_parsed
