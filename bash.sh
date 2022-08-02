

#!/bin/bash

echo "-------------------------------Docker Container Services-------------------------------"

echo "Services: Start Docker (start), Remove Docker (remove) and Show Docker Status (status)"

echo "Enter the service you want"
read service

function start() {
    echo "Building container"
    docker build -t jenkins .
    echo "Starting container"
    docker run -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock --name jenkins jenkins
}

function remove() {
    echo "removing image"
    docker rmi jenkins --force
    echo "image removed"
    echo "removing container"
    docker rm jenkins --force
    echo "container removed"
}

function status() {
    echo "docker status:"
    docker container inspect jenkins | grep Status
    echo "docker container info:"
    docker ps -a -f  name=jenkins
}

function key() {
    echo "searching the initial key"
    docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
}

case $service in
    start)
        start;;
    remove)
        remove;;
    status)
        status;;
    key)
        key;;
    *)
        echo "This service does not exist"
esac 
