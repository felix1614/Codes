import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# n = int(input())
# if type(round(n/2))=="float":
#     print(round(n/2)+n)
# else:
#     print(round(n/2+n))
n = 5
print(type(n))
if type(round(n/2))==float:
    print(round(n/2)+n)
if type(round(n/2))==int:
    print(round(n/2)+n)
elif n==1:
    print(1)
else:
    print(round(n/2+n))