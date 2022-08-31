"""
The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
Input
0 0
1
N 1
Expected output
0 1

Input
0 0
4
N 1
E 1
S 1
W 1
Expected output
0 0

Input
-12 -8
2
E 10
S 3
Expected output
-2 -11

Input
-33 18
8
W 100
S 100
E 100
N 100
E 100
N 100
W 100
S 100
Expected output
-33 18
"""
# a, b = -12, -8
# c, d = "E 10", "S 3"    #-2 -11
x, y = [int(i) for i in input().split()]
n = int(input())
for i in range(n):
    inputs = input().split()
    dirc = inputs[0]
    dist = int(inputs[1])
    if dirc == 'N':y+=dist
    elif dirc == 'E':x+=dist
    elif dirc == 'S':y-=dist
    elif dirc == 'W':x-=dist
print(x,y)