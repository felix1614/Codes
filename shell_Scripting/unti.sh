#!/bin/bash
A=10;until ((A<10));do echo $A; A=`expr $A + 1`;if ((A==30));then break;fi;done
