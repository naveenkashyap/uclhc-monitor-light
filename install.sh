#! /bin/bash

echo "Installing Factory Monitoring System"

mkdir /var/lib/factory-monitor
mkdir /var/lib/factory-monitor/outboxes
mkdir /var/cache/factory-monitor
mkdir /var/log/factory-monitor
cp factory-monitor /etc/init.d
cp factory-monitord /usr/sbin
cp monitor.py /var/lib/factory-monitor
cp config.json /var/lib/factory-monitor
cp metrics.py /var/lib/factory-monitor

echo "Installation finished"
