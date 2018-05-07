#!/bin/bash

echo "pull.sh started..."
# once the images are on the server its easier to just pull them

STR=`date +"%m%d%Y"`

time docker pull thesheff17/docker_base:lts_latest-$STR
time docker pull thesheff17/docker_base:lts_gui_latest-$STR
time docker pull thesheff17/docker_base:rolling_latest-$STR
time docker pull thesheff17/docker_base:rolling_gui_latest-$STR

echo "pull.sh completed."
