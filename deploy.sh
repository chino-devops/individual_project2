#!/bin/bash

project_name=individual_project2

# Build server
docker build -t ${project_name}_server server
# watch_services
docker build -t ${project_name}_api watch_api
# create network
docker network create ${project_name}_network
# Run containers
docker run -d \
    - p 5000:5000
    --name ${project_name}_server \
    --network ${project_name}_network \
    ${project_name}_server

docker run -d \
    - p 5000:5000
    --name ${project_name}_api \
    --network ${project_name}_network \
    ${project_name}_api 


