"""

The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:

Test 1
Input
11
HFNOS CVZUN
Expected output
HELLO WORLD

Test 2
Input
9
CPFLRLGTM
Expected output
CODINGAME

Test 3
Input
9
EYEHPQKUB
Expected output
EXCELLENT

Test 4
Input
8
ACEGI!!!
Expected output
ABCDE!!!

"""
message = "ACEGI!!!"
c=""
for i in range(len(message)):
    if message[i].isalpha():
        c += (chr((ord(message[i])-i-65)%26+65))
    else:
        c += message[i]
        # c+=chr(i-(ord(message[i])))
print(c)

