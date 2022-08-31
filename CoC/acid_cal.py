import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

acid_name = input()
acid_count = int(input())
water_count = int(input())
a=["Hydrochloric,Sulfuric,Nitric,Citric"]
if  acid_name in a:
    c=(acid_count/(acid_count+water_count))*100
    print(c)
