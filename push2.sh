#!/bin/bash

echo "push.sh started..."

time docker push thesheff17/docker_base:lts_latest-`date +"%m%d%Y"`
time docker push thesheff17/docker_base:lts_gui_latest-`date +"%m%d%Y"`
time docker push thesheff17/docker_base:rolling_latest-`date +"%m%d%Y"`
time docker push thesheff17/docker_base:rolling_gui_latest-`date +"%m%d%Y"`

echo "push.sh completed."
