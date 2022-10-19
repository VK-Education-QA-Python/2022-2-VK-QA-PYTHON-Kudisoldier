EMAIL = '2jorzjylbglw@mail.ru'
PASSWORD = '2jorzjylbglw'


def get_credentials():
    return EMAIL, PASSWORD


def driver_load_requests_session(driver, requests_session):
    for cookie in requests_session.cookies:
        driver.add_cookie({
            'name': cookie.name,
            'expiry': cookie.expires,
            'path': cookie.path,
            'value': cookie.value
        })
