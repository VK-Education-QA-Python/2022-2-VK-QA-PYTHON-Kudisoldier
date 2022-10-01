import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


LOGIN = '2jorzjylbglw@mail.ru'
PASSWORD = '2jorzjylbglw'


def login_with_credentials(driver, login, password):
    driver.get('https://target-sandbox.my.com')
    login_form_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'responseHead-module-button')]"))
    )
    login_form_button.click()

    login_input = driver.find_element(By.XPATH, "//input[@name = 'email']")
    login_input.clear()
    login_input.send_keys(login)

    login_input = driver.find_element(By.XPATH, "//input[@name = 'password']")
    login_input.clear()
    login_input.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//div[contains(@class, 'authForm-module-button')]")
    login_button.click()


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="105.0.5195.19").install()))
    yield driver
    driver.close()


@pytest.fixture
def session(driver):
    login_with_credentials(driver, LOGIN, PASSWORD)
    yield driver
