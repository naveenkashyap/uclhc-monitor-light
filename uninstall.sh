#! /bin/bash

# TODO Check service is not currently running
echo "Uninstalling Factory  Monitoring System"

rm /etc/init.d/factory-monitor
rm /usr/sbin/factory-monitord
rm -r /var/lib/factory-monitor
rm -r /var/log/factory-monitor
rm -r /var/cache/factory-monitor

echo "Uninstallation finished"

