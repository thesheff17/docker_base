#!/bin/bash

echo "save.sh started..."

docker save thesheff17/docker_base:lts_latest | gzip > lts_latest.tgz
docker save thesheff17/docker_base:lts_gui_latest | gzip > lts_gui_latest.tgz
docker save thesheff17/docker_base:rolling_latest | gzip > rolling_latest.tgz
docker save thesheff17/docker_base:rolling_gui_latest | gzip > rolling_gui_latest.tgz

echo "save.sh completed."
