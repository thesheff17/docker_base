#!/bin/bash

echo "build.sh started..."


# lts
time docker build -f Dockerfile-lts . -t thesheff17/docker_base:lts_latest
time docker build -f Dockerfile-lts-gui . -t thesheff17/docker_base:lts_gui_latest

# rolling
time docker build -f Dockerfile-rolling . -t thesheff17/docker_base:rolling_latest
time docker build -f Dockerfile-rolling-gui . -t thesheff17/docker_base:rolling_gui_latest

echo "build.sh completed."
