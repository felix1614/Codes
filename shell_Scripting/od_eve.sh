#!/bin/bash
read -p "Enter no: " A
for C in $(seq 1 $A)    #for ((C=1;C<=A;C++))
do
  if ((C%2==0))
  then
    echo "EVEN $C"
  else
    echo "ODD $C"
  fi
done