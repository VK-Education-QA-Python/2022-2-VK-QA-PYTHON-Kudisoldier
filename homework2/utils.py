def get_credentials():
    with open("credentials.txt", "r") as file:
        return file.read().split(':')


def driver_load_requests_session(driver, requests_session):
    for cookie in requests_session.cookies:
        driver.add_cookie({
            'name': cookie.name,
            'expiry': cookie.expires,
            'path': cookie.path,
            'value': cookie.value
        })
