#!/bin/sh
echo "Deploying Theiox 2.0 services"

# shacalc cmd ==> find theiox/alarm_service/ -type f -exec sha512sum {} \; | sha512sum | awk '{print $1}'

file_down(){
  echo "Downloading Hash_codes for $1"
  wget  -q "https://docs.google.com/spreadsheets/d/1ACz6hoBqhm0AI5IUbzsDw3IwGXCiwB2e-0gQF1BEKjo/export?format=csv&gid=808450103" -O /home/"$(echo "$(echo "$(w -h -s)" | cut -c1-9)" | xargs)"/PycharmProjects/CodingManiac/shell_Scripting/Hash_codes.csv
  if [ -f /home/"$(echo "$(echo "$(w -h -s)" | cut -c1-9)" | xargs)"/PycharmProjects/CodingManiac/shell_Scripting/Hash_codes.csv ];then echo "Hash_codes downloaded for $1";else echo "error downloading Hash_codes";exit 90;fi
}
Hashi(){
  INPUT=Hash_codes.csv
  OLDIFS=$IFS
  IFS=','
  if [ ! -f $INPUT ];then file_down "$2";else rm "$INPUT";file_down "$3" "$2";fi
  while read -r SNAME HASH
  do
    if [ "$SNAME" = "$2" ];then
#      echo "$NAME"
      SHA="$(find $1 -type f -exec sha512sum {} \; | sha512sum | awk '{print $1}' )"
#      echo "$SHA"
      if [ "$(echo "$HASH" | cut -c1-128)" = "$SHA" ]; then echo "No Change Detected in $NAME";rm "$INPUT";else echo "change Detected in $NAME";rm "$INPUT";exit 0;fi
      fi
  done < $INPUT
  IFS=$OLDIFS
}

for FOLD in theiox/*
do
  NAME="$(basename "$(find $FOLD -executable -type f)")"
  Hashi $FOLD/ $NAME
done

sudo cp -r theiox/* /theiox
sudo cp -r service_files/* /etc/systemd/system

echo "Deploying Theiox UI"
rm -rf /usr/share/nginx/html/*
sudo cp -r elmeasure_ui/* /usr/share/nginx/html

echo "Adding Nginx Configuration"
sudo rm -rf /etc/nginx/nginx.conf
sudo cp -r nginx.conf /etc/nginx


echo "Service Enabling AND Restart"
sudo systemctl enable theiox_aggregator.service
sudo systemctl start theiox_aggregator.service

sudo systemctl enable theiox_alarm.service
sudo systemctl start theiox_alarm.service

sudo systemctl enable theiox_api.service
sudo systemctl start theiox_api.service

sudo systemctl enable theiox_asset_onboard.service
sudo systemctl start  theiox_asset_onboard.service

sudo systemctl enable theiox_daq_controller.service
sudo systemctl start theiox_daq_controller.service

sudo systemctl enable theiox_bacnet_daq.service
sudo systemctl start theiox_bacnet_daq.service

sudo systemctl enable theiox_dashboard.service
sudo systemctl start theiox_dashboard.service

sudo systemctl enable theiox_gw3k_to_theiox.service
sudo systemctl start theiox_gw3k_to_theiox.service

sudo systemctl enable theiox_license_automate.service
sudo systemctl start theiox_license_automate.service

sudo systemctl enable theiox_license_controller.service
sudo systemctl start theiox_license_controller.service

sudo systemctl enable  theiox_manual_entry_excel.service
sudo systemctl start  theiox_manual_entry_excel.service

sudo systemctl enable  theiox_modbus_daq.service
sudo systemctl start  theiox_modbus_daq.service

sudo systemctl enable theiox_mqtt.service
sudo systemctl start theiox_mqtt.service

sudo systemctl enable theiox_mqtt_gw.service
sudo systemctl start theiox_mqtt_gw.service

sudo systemctl enable theiox_opcua_daq.service
sudo systemctl start theiox_opcua_daq.service

sudo systemctl enable theiox_reports.service
sudo systemctl start theiox_reports.service

sudo systemctl enable theiox_snmp_daq.service
sudo systemctl start theiox_snmp_daq.service

sudo systemctl enable theiox_system_info.service
sudo systemctl start theiox_system_info.service

sudo systemctl restart nginx emqx mongod

echo "Theiox 2.0 Deployment Completed"
