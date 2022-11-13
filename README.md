## Homework 6 - testing database with ORM
Steps to run homework6:
```
docker run --name TEST_SQL -p 3306:3306 -e MYSQL_ROOT_PASSWORD=pass -d mysql:8.0
pytest homework6 -n 2
```

Contents:
- All data from HW 5 tested

Features:
- support multiple CPU runs
- test written with pytest
- used MySql database
