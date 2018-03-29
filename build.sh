#!/bin/bash

echo "build.sh started..."

cd "docker_base"
git pull

# lts
time docker build -f Dockerfile-lts . -t thesheff17/docker_base:lts_latest
time docker build -f Dockerfile-lts-gui . -t thesheff17/docker_base:lts_gui_latest

# rolling
time docker build -f Dockerfile-rolling . -t thesheff17/docker_base:rolling_latest
time docker build -f Dockerfile-rolling-gui . -t thesheff17/docker_base:rolling_gui_latest

# docker tag
docker tag thesheff17/docker_base:lts_latest thesheff17/docker_base:lts-`date +"%m%d%Y"`
docker tag thesheff17/docker_base:lts_gui_latest  thesheff17/docker_base:lts_gui-`date +"%m%d%Y"`
docker tag  thesheff17/docker_base:rolling_latest  thesheff17/docker_base:rolling-`date +"%m%d%Y"`
docker tag thesheff17/docker_base:rolling_gui_latest thesheff17/docker_base:rolling_gui-`date +"%m%d%Y"`

# docker push
docker push thesheff17/docker_base:lts_latest
docker push thesheff17/docker_base:lts_gui_latest
docker push thesheff17/docker_base:rolling_latest
docker push thesheff17/docker_base:rolling_gui_latest
docker push thesheff17/docker_base:lts-`date +"%m%d%Y"`
docker push thesheff17/docker_base:lts_gui-`date +"%m%d%Y"`
docker push thesheff17/docker_base:rolling-`date +"%m%d%Y"`
docker push thesheff17/docker_base:rolling_gui-`date +"%m%d%Y"`

echo "build.sh completed."
