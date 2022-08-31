import sys
import math

# Auto-generated code below aims at helping you parse
a=[]
for i in range(3):
    for j in input().split():
        if j.isalpha():
            a.append(j.upper())
if a.count("X"):
    if a[-1]=="X":
        print("O")
    else:
        print("X")
else:
    print("X")

# len(a[j:j+4]) is 4 and

