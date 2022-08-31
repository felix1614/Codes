#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    c = [0, 0]
    for i in zip(a,b):
        if i[0]>i[1]:
            c[0]+=1
        elif i[0]==i[1]:
            pass
        elif i[0]<i[1]:
            c[1]+=1
    return c


if __name__ == '__main__':

    a =[5,2,3]

    b = [3,2,1]

    result = compareTriplets(a, b)
    print(result)