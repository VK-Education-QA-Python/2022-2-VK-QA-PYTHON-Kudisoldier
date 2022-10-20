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
pytest -v -m UI --headless -n 3 --alluredir allure
```
Steps to view allure report:
```
allure serve allure
```
Steps to run selenoid:
```
add --selenoid option to pytest
./cm_darwin_amd64 selenoid-ui start

pytest --selenoid -n 3

OR for my mac m1

docker run -d                                   \
--name selenoid                                 \
-p 4444:4444                                    \
-v /var/run/docker.sock:/var/run/docker.sock    \
-v `pwd`/config/:/etc/selenoid/:ro              \
--privileged                                    \
aerokube/selenoid:latest-release                \
-service-startup-timeout 1m

docker run -d         \
    --name selenoid-ui  \
    --link selenoid     \
    -p 8080:8080        \
    aerokube/selenoid-ui --selenoid-uri=http://selenoid:4444
```

Contents:
- advertising campaign test
- creation of segment with audience in app test
- creation of segment with vk edu group test

Features:
- runnable in selenoid
- support multiple CPU runs
- automatic allure reports
- written with PageObject pattern
- login with api call