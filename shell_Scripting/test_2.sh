#!/bin/sh

#CDS="$(echo $USER)"
#echo "$CDS"
. /home/"$(echo "$(echo "$(w -h -s)" | cut -c1-9)" | xargs)"/PycharmProjects/CodingManiac/shell_Scripting/Hashing.sh
[ ! -d /tmp/ilens/tar/ ] && { echo "inside dir";mkdir -p /tmp/ilens/tar;cp ~/Downloads/releases/alarm_service.tar.gz /tmp/ilens/tar; cp ~/Downloads/releases/meta_services_2.tar.gz /tmp/ilens/tar; }
#~/PycharmProjects/CodingManiac/venv/bin/python ~/PycharmProjects/CodingManiac/dash/dash_4.py "hi"

Hashing /home/afnan/Downloads/releases/meta_services_2.tar.gz meta_services_2 1ACz6hoBqhm0AI5IUbzsDw3IwGXCiwB2e-0gQF1BEKjo 0
#Hashing /home/afnan/Downloads/elmeasure_ui.tar.gz elmeasure_ui 1ACz6hoBqhm0AI5IUbzsDw3IwGXCiwB2e-0gQF1BEKjo 0


#NUMBER=$(echo "The store is 1.2 miles away." | tr -dc '0-9') ; echo $NUMBER
#NUMBER=$(echo "The store is 1.2 miles away" | sed 's/[^0-9][.][^0-9]*//g') ; echo $NUMBER
#NUMBER=$(echo "The store is 1.2 miles away." | grep -Eo '[0-9]+([.][0-9]+)?')$? ; echo $NUMBER

#echo "12.3" | grep "^[0-9]*[.][0-9]*"
#OIFS=$IFS
#IFS=' '
#for x in $(tar -axf /home/afnan/Downloads/elmeasure_ui.tar.gz elmeasure_ui/release_notes.txt -O)
#do
#  echo "$x"
#  ADS=$(echo "$x" | grep -E "^[0-9]*[.][0-9]*")$?
#  echo "$ADS"
#  if [ $ADS != 1 ];then
#    echo "$x"
#    echo "$ADS, $x"
#  fi
#  val=`"$ADS" $?`
#  echo "$val"
#done
#IFS=$OIFS
#val=123.3
#if [ $val = 0 ]
#then
#        echo "Given string is float"
#else
#        echo "Invalide"
#fi









#Hashing /tmp/ilens/tar/meta_services_2.tar.gz meta_services_2 1ACz6hoBqhm0AI5IUbzsDw3IwGXCiwB2e-0gQF1BEKjo
#DS="$(echo "$(echo "$(w -h -s)" | cut -c1-9)" | xargs)"
#echo "$DS"
#echo "$SHA_1"
#DSS="$(echo "$(echo "$(w -h -s)" | cut -c1-9)" | xargs)"
#echo "$DSS"
#wget -q "https://docs.google.com/spreadsheets/d/1ACz6hoBqhm0AI5IUbzsDw3IwGXCiwB2e-0gQF1BEKjo/export?format=csv&gid=0" -O "hash_codes.csv"
#if [ "linu" = "linux" | sed 's/.$//' ];then
#  echo "hello"
#t="lkj"
#if [ "lk" = ${t%?} ];then
#  echo "${t%?}"
#fi