# VK SDET homeworks

## Homework 1 - testing web UI with selenium
Steps to run homework1:
```
cd homework 1
pytest -v -m UI --headless
```

Contents:
- login test
- logout test
- 2 login negative test
- change contacts test
- 2 parametrized menu page navigation

## Homework 2 - testing web UI with selenium and PageObject pattern
Steps to run homework2:
```
cd homework 2
pytest -v -m UI --headless -n 3
```

Contents:
- advertising campaign test
- creation of segment with audience in app
- creation of segment with vk edu group

Features:
- runnable in selenoid
- support multiple CPU runs
- automatic allure reports
- written with PageObject pattern
- login with api call