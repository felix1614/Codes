"""
The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
npqrst
o
02 Test 2
Input
Expected output
DEADBEEF
C
03 Test 3
Input
Expected output
azertyuiopqsdfghjklmwxcvb
n
04 Test 4
Input
Expected output
./09:;<
12345678
05 Test 5
Input
Expected output
Yeux
Z[\]^_`abcdfghijklmnopqrstvw
"""

message="Yeux"

d=[]
for i in range(ord(message[0]), ord(message[-1])):
    if chr(i) not in message:
        d += chr(i),
print("".join(d))




