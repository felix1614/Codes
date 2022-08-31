'''The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
Expected output
2
4
[1,2]
[3,4]
[5,6]
[7,8]
02 Test 2
Input
Expected output
9
2
[1,2,3,4,5,6,7,8,9]
[10,11,12,13,14,15,16,17,18]
03 Test 3
Input
Expected output
10
5
[1,2,3,4,5,6,7,8,9,10]
[11,12,13,14,15,16,17,18,19,20]
[21,22,23,24,25,26,27,28,29,30]
[31,32,33,34,35,36,37,38,39,40]
[41,42,43,44,45,46,47,48,49,50]
04 Test 4
Input
Expected output
5
1
[1,2,3,4,5]'''
l = 5
n = 10
c=[]
e=0
for i in range(n):
    c.append([j for j in range(e+1,e+l+1)])
    e=c[len(c)-1][1]
for i in c:
    print(i)