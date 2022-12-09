#!/bin/bash

docker run --hostname appmysqldb --name mysqldb -e MYSQL_ROOT_PASSWORD=pass -p 3306:3306 -d mysql:latest

while ! docker exec mysqldb mysql --user=root --password=pass -e "SELECT 1" >/dev/null 2>&1; do
    sleep 1
done

docker exec mysqldb mysql --user=root --password=pass -e \
"CREATE DATABASE myappdb;
use myappdb;
CREATE TABLE "test_users" (
  "id" int NOT NULL AUTO_INCREMENT,
  "name" varchar(255) NOT NULL,
  "surname" varchar(255) NOT NULL,
  "middle_name" varchar(255) DEFAULT NULL,
  "username" varchar(16) DEFAULT NULL,
  "password" varchar(255) NOT NULL,
  "email" varchar(64) NOT NULL,
  "access" smallint DEFAULT NULL,
  "active" smallint DEFAULT NULL,
  "start_active_time" datetime DEFAULT NULL,
  PRIMARY KEY ("id"),
  UNIQUE KEY "email" ("email"),
  UNIQUE KEY "ix_test_users_username" ("username")
);
CREATE USER 'test_qa'@'%' IDENTIFIED BY 'qa_test';
GRANT ALL PRIVILEGES ON myappdb.* TO 'test_qa'@'%';
FLUSH PRIVILEGES;"

if ! docker image inspect myapp >/dev/null 2>&1; then
  docker load -i myapp
fi

export setup_pwd=`pwd`
export mock_pwd=`cd $setup_pwd/../mock; pwd`
cd $mock_pwd
./build_docker.bash

docker run --name myapp -v $setup_pwd/config.ini:/etc/config.ini -p 1000:1000 --link mysqldb:appmysqldb  --link vk_api:vk_id_mock myapp /app/myapp --config=/etc/config.ini
