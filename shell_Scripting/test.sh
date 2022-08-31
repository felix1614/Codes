#!/bin/bash

shm_id=$(sha256sum  /home/afnan/Downloads/releases/alarm_service/alarms_events_service | awk '{print $1}')
echo $shm_id
