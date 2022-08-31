#!/bin/bash
#echo "Hi"
#read PERSON
#echo "hello $PERSON"
#NAME="BYE"
#unset NAME  #removes the value of  a variable
#echo $NAME
#echo $$   #$$ defines the PID
#echo $0   #$0 ==> current shell_script name
#echo $#   #$# ==> Total no.of arguments sends to the script
#echo $?   #exit status of the script  0-> success, 1->Fail
#echo $!   #The process number of the last background command

#echo "First Param: $1"
#echo "second Param: $2"
#echo "Total Param: $#"

#for TOKEN in $*     #if the cmd has unlimited arg/. can use for loop
#do
#  echo $TOKEN
#done
#declare -a NAME
#echo "Arithmetic Operations"
#read -p "Enter num_1: " NAME[0]
#read -p "Enter num_2: " NAME[1]
#NAME[2]="Beast"
#echo "${NAME[0]} ${NAME[1]}"
#echo "${NAME[@]}"

#echo "total ${NAME[0]} and ${NAME[1]} is $((NAME[0]+NAME[1]))"

#if(((( ${NAME[0]} <= ${NAME[1]} )) & ((${NAME[0]} == ${NAME[1]}))));then echo "true";else echo "false";fi

echo -e "1:Add         2:SUB\n3:MUL         4:Div\n5:equals      6:Not Equal\n7:lesserThan  8:GreaterThan"

read -p "Enter Your Choice: " C
read -p "Enter num_1: " A
read -p "Enter num_2: " B

case $C in 1) echo "$((A+B))";;
2) echo "$((A-B))";;
3) echo "$((A*B))";;
4) echo "$((A/B))";;
5) if(((( A==B))==1));then echo "True";else echo "False";fi;;
6) if(((( A!=B))==1));then echo "True";else echo "False";fi;;
7) if(((( A<B))==1));then echo "True";else echo "False";fi;;
8) if(((( A>B))==1));then echo "True";else echo "False";fi;esac



