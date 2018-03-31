#!/bin/bash

echo "build.sh started..."


# first set
time docker build -f Dockerfile-lts . -t thesheff17/docker_base:lts_latest &
time docker build -f Dockerfile-rolling . -t thesheff17/docker_base:rolling_latest &
wait

# second set
time docker build -f Dockerfile-rolling-gui . -t thesheff17/docker_base:rolling_gui_latest &
time docker build -f Dockerfile-lts-gui . -t thesheff17/docker_base:lts_gui_latest &
wait

echo "build.sh completed."
