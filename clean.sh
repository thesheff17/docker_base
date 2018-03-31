#!/bin/bash
echo "clean.sh started..."

docker stop $(docker ps | grep docker_base* | cut -f1 -d" ")
docker rm $(docker ps | grep docker_base* | cut -f1 -d" ")
docker rmi $(docker images | grep "docker_base" | awk "{print \$3}")

docker ps -a
docker images

echo "clean.sh completed."
