#!/bin/sh
echo "success"

file_down(){
  echo "Downloading Hash_codes for $2"

  wget  -q "https://docs.google.com/spreadsheets/d/$1/export?format=csv&gid=0" -O /home/"$(echo "$(echo "$(w -h -s)" | cut -c1-9)" | xargs)"/PycharmProjects/PersonalActivity/shell_Scripting/Hash_codes.csv
  if [ -f /home/"$(echo "$(echo "$(w -h -s)" | cut -c1-9)" | xargs)"/PycharmProjects/PersonalActivity/shell_Scripting/Hash_codes.csv ];then echo "Hash_codes downloaded for $2";else echo "error downloading Hash_codes";exit 90;fi
}

Hashing()
{
OIFS=$IFS
IFS=' '
#for x in $(cat /tmp/ilens/untar/"$1")
for x in $(tar -axf "$1" "$2"/release_notes.txt -O)
do
#  ADS=$(echo "$x" | grep -E "^[0-9]*[.][0-9]*")
  if [ "$2" = "elmeasure_ui" ];then
  ADS=$(echo "$x" | grep -Eo '[0-9]+([.][0-9]+)?')$?;x=$(echo "$x" | grep -Eo '[0-9]+([.][0-9]+)?');else ADS=1;fi
  if [ "x." = "$(echo "$x" | cut -c -2)" ] || [ $ADS != 1 ];then
    echo "$x, $ADS"
    INPUT=Hash_codes.csv
    OLDIFS=$IFS
    IFS=','
    if [ ! -f $INPUT ];then file_down "$3" "$2";fi
    while read -r flname release HASHC
    do
      if [ "$flname" = "$2" ] && [ "$x" = "$release" ]
      then
#        echo "$flname, $x"
        SHA=$(sha512sum  "$1" | awk '{print $1}')
        echo "$SHA"
        if [ "$(echo "$HASHC" | cut -c1-128)" = "$SHA" ]
        then echo "No Change Detected in $flname";else echo "change Detected in $flname";exit 0;fi;fi
    done < $INPUT
    IFS=$OLDIFS
    fi
done
IFS=$OIFS
}

#lunedi
#martedi
#marcoledi
#geovedi
#venerdi
#sabato
#domenica