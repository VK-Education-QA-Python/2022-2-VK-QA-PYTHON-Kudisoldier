from base import *

USERNAME_DEFAULT = '2jorzjylbglw@mail.ru'
PASSWORD_DEFAULT = '2jorzjylbglw'


def login(driver, username=USERNAME_DEFAULT, password=PASSWORD_DEFAULT):
    driver.get('https://target-sandbox.my.com')

    wait_until_page_loaded(driver)

    click(driver, locators.LOGIN_FORM_BUTTON)

    fill_input(driver, locators.LOGIN_INPUT, username)
    fill_input(driver, locators.PASSWORD_INPUT, password)

    click(driver, locators.LOGIN_BUTTON)
