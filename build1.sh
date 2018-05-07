#!/bin/bash

echo "build1.sh started..."

time docker build -f Dockerfile-lts . -t thesheff17/docker_base:lts_latest-`date +"%m%d%Y"`

echo "build1.sh completed."