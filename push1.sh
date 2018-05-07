#!/bin/bash

echo "push1.sh started..."

time docker push thesheff17/docker_base:lts_latest-`date +"%m%d%Y"`

echo "push1.sh completed."
