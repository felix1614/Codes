'''Using an input number n, a size s and and an offset o, write s lines containing s numbers representing each character the offset from the previous number. If the grid is empty, return "Nothing".
Input
Line 1: An n integer representing the start number (top left)
Line 2: An s integer representing the size of the grid
Line 3: An o integer representing the offset.
Output
s lines: representing the grid or "Nothing" if the grid is empty.
Constraints
0≤s≤1000
-10<o≤10
Example
Input
5
2
1
Output
5 6
6 7

Input
10
10
3

Output
10 13 16 19 22 25 28 31 34 37
13 16 19 22 25 28 31 34 37 40
16 19 22 25 28 31 34 37 40 43
19 22 25 28 31 34 37 40 43 46
22 25 28 31 34 37 40 43 46 49
25 28 31 34 37 40 43 46 49 52
28 31 34 37 40 43 46 49 52 55
31 34 37 40 43 46 49 52 55 58
34 37 40 43 46 49 52 55 58 61
37 40 43 46 49 52 55 58 61 64
Input
500
0
10
Output
Nothing
Input
50
6
-2
Output
50 48 46 44 42 40
48 46 44 42 40 38
46 44 42 40 38 36
44 42 40 38 36 34
42 40 38 36 34 32
40 38 36 34 32 30
'''

n = 10
s = 5
o = 3
e=n
d=[]
for i in range(s):
    for j in range(s):
        d.append([e])
        print(e, end=" ")
        e+=o
    if len(d)==s:
        for i in range(s):
            if i==0:
                e=0
                print()
            print(d[1][0]+e,end=" ")
            e += o
        d.clear()
    print()



