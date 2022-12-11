from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "browserVersion": "100.0",
    "selenoid:options": {
        "enableVideo": False,
        "enableVNC": True
    }
}

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities)

driver.get('http://myapp:1000/login')
html = driver.page_source
print(html)
