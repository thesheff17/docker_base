#!/bin/bash

echo "build.sh started..."

time docker build -f Dockerfile-lts-gui CHANGEDATE=`date +"%m%d%Y"` . -t thesheff17/docker_base:lts_gui_latest-`date +"%m%d%Y"`
time docker build -f Dockerfile-rolling . -t thesheff17/docker_base:rolling_latest-`date +"%m%d%Y"`
time docker build -f Dockerfile-rolling-gui CHANGEDATE=`date +"%m%d%Y"` . -t thesheff17/docker_base:rolling_gui_latest-`date +"%m%d%Y"`

echo "build.sh completed."
