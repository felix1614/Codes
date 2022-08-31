"""
The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1
Input
4
0 1 3 1 3 1 0
Expected output
*     *  ****
** * **  *  *
** * **  *  *
*************
02 Test 2
Input
5
0 1 0 1 0 1 0 1 0 1 0
Expected output
* * * * * *  ****
***********  *  *
***********  *  *
***********  *  *
*****************
03 Test 3
Input
6
5 4 3 2 1 0
Expected output
     *  ****
    **  *  *
   ***  *  *
  ****  *  *
 *****  *  *
************
04 Test 4
Input
4
0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0
Expected output
******** ********  ****
******** ********  *  *
******** ********  *  *
***********************
"""


height = int(input())
specs = input().split(' ')
output = []
for i in range(height):
    output.append("")

for item in specs:
    h = int(item)
    for i in range(height):
        if i >= h:
            output[i] += '*'
        else:
            output[i] += ' '

for i in range(height):
    if i == 0:
        output[i] += '  ****'
    elif i == height - 1:
        output[i] += '******'
    else:
        output[i] += '  *  *'

for out in output:
    print(out)
