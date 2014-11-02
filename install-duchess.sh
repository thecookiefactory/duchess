#!/bin/bash

apt-get update
apt-get install git curl wget vim -y
apt-get install python3-dev python3-pip redis-server -y

pip3 install -r /vagrant/requirements.txt

read -rd '' INIT_SCRIPT <<EOF
description "Duchess"
author "Bence Nagy <bence@underyx.me>"
start on runlevel [2345]
stop on runlevel [!2345]

respawn
exec start-stop-daemon --start --chdir /vagrant --exec /usr/local/bin/invoke -- start
EOF

echo -e "$INIT_SCRIPT" > /etc/init/duchess.conf

service duchess start
