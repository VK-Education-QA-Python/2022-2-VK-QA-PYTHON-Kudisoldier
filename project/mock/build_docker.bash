#!/bin/bash

docker build -t vk_api .
docker run --hostname vk_id_mock --name vk_api -p 777:777 -d vk_api:latest
