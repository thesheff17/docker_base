#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018, Dan Sheffner Digital Imaging Software Solutions, INC
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""
This program will build a local docker registry

*** WARNING! This will delete all your local docker containers and images! ***

"""

from subprocess import check_output as co
from subprocess import run
import os
import time


class Registry(object):
    """
    This class will build a docker registry
    """

    version = '0.1'

    def __init__(self):

        # This will be the registry DNS name you can pull from
        # You can use a FQDN. or use host file
        self.fake_dns = "dockerregistry:5000"

        # helper for date on thesheff17 images
        base_image_date = '03312018'

        # we should check to see if you have better push settings
        docker_file = "/etc/default/docker"
        if os.path.isfile(docker_file):
            search = "--max-concurrent-uploads"
            if search in open(docker_file).read():
                print("Found good max concurrent upload settings.")
            else:
                # this should go in /etc/defaut/docker
                # DOCKER_OPTS="--max-concurrent-uploads 10"
                # service docker restart
                print("*** WARNING You should set --max-concurrent-uploads to speed things up. ***")

        # no tag at end assumes latest
        self.images = [
            'alpine',
            'amazonlinux',
            'couchbase/server:enterprise-4.6.3',
            'centos',
            'debian',
            'elcolio/etcd',
            'haproxy',
            'httpd',
            'influxdb',
            'jupyter/base-notebook',
            'jenkins',
            'memcached',
            'mysql:5.6',
            'mysql:5.7',
            'mysql',
            'nginx',
            'python:3.6.4-stretch',
            'python:3.7.0a4',
            'golang:alpine',
            'golang',
            'gopherdata/gophernotes-ds',
            'grafana/grafana',
            'ruby:2.4.0',
            'ruby',
            'scylladb/scylla',
            'ubuntu',
            'ubuntu:16.04',
            'ubuntu:rolling',
        ]

        custom_images = [
            'thesheff17/apt-cacher-ng',
            'thesheff17/docker_dev:20180402',
            'thesheff17/docker_dev',
            'thesheff17/docker_base:rolling_gui-' + base_image_date,
            'thesheff17/docker_base:rolling-' + base_image_date,
            'thesheff17/docker_base:lts_gui-' + base_image_date,
            'thesheff17/docker_base:lts-' + base_image_date,
            'thesheff17/docker_base:rolling_gui_latest',
            'thesheff17/docker_base:rolling_latest',
            'thesheff17/docker_base:lts_gui_latest',
            'thesheff17/docker_base:lts_latest']

        self.images.extend(custom_images)

        # for testing a single container
        # self.images = [
        #    'thesheff17/apt-cacher-ng',]

    def cleanup_docker_containers(self):
        command1 = "docker ps | wc -l"
        output1 = co(command1, shell=True)
        if int(output1) > 1:
            command2 = "docker stop $(docker ps -a -q)"
            run(command2, shell=True)

        command3 = "docker ps -a | wc -l"
        output2 = co(command3, shell=True)
        if int(output2) > 1:
            command4 = "docker rm -f $(docker ps -a -q)"
            run(command4, shell=True)

    def clean_all(self):
        command1 = "docker images | wc -l"
        output1 = co(command1, shell=True)
        if int(output1) > 1:
            command2 = "docker rmi -f $(docker images -q)"
            run(command2, shell=True, check=False)

    def create_registry(self):
        command1 = "docker run -d -p 5000:5000 --restart=always --name registry registry:2"
        run(command1, shell=True, check=True)

    def start(self):
        time.sleep(5)
        for each in self.images:

            command1 = "docker pull " + each
            run(command1, shell=True, check=True)

            command1 = "docker tag " + each + " localhost:5000/" + each
            run(command1, shell=True, check=True)

            command1 = "docker push localhost:5000/" + each
            run(command1, shell=True, check=True)

            # command1 = "docker rmi -f " + each
            # run(command1, shell=True, check=True)

    def generate_pull_script(self):
        # script to pull images
        with open("./pull_script.sh", "w") as file:
            file.write("#!/bin/bash\n")
            file.write("\n")
            file.write('echo "pull_script.sh started..."\n\n')

            for each in self.images:
                file.write("docker pull " + self.fake_dns + "/" + each + "\n")

            file.write("\n")

            for each in self.images:
                file.write("docker tag " +  self.fake_dns + "/" + each + " " + each + "\n")

            file.write("\n")
            file.write('echo "pull script.sh completed."')

        run("chmod +x pull_script.sh", shell=True, check=True)

if __name__ == "__main__":
    print("buildRegistry.py started...")
    start = time.time()

    registry = Registry()
    registry.cleanup_docker_containers()
    registry.clean_all()
    registry.create_registry()
    registry.start()
    registry.generate_pull_script()

    done = time.time()
    elapsed = done - start
    total_time = str(elapsed/60).split('.')[0]

    print("buildRegistry.py completed. Elapse time: " + str(total_time) + " mins.")