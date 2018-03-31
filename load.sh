#!/bin/bash

echo "load.sh started..."

gunzip -c lts_latest.tgz |  docker load
gunzip -c lts_gui_latest.tgz | docker load
gunzip -c rolling_latest | docker load
gunzip -c rolling_gui_latest | docker load

echo "load.sh completed."
