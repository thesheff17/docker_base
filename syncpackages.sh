#!/bin/bash

echo "syncPackages.sh started..."

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# set your host file to the cache server
# this hides the EC2 DNS name
rsync -r -a -e ssh --progress --delete root@cache:/var/cache/apt-cacher-ng /var/cache/apt-cacher-ng

echo "syncPackages.sh completed."
