"""
You are given a set of lines, each line containing a set of operations separated by a semicolon (";"). For each line, you must calculate the result of all operations and print their sum.

All "+", "-", "*" and "/" operations can be performed.

The result of each line should be rounded to the nearest integer.

Negative numbers are taken into account.
Input
Line 1: An integer N for the number of lines containing the operations.
Next N lines: a string of characters presenting the operations separated with semicolon.
Output
N lines: each contain the sum of the operations' results as an integer.
Constraints
1 ≤ N ≤ 10
Example
Input
1
1+1+2;2*2;3-1
Output
10

TESt:2
2
100
2-100;200

OUTPUT:
100
102
"""


l=0
k=input
for i in range(2):
    for j in k("enter str: ").split(";"):l+=eval(j)
    k(round(l))
    l=0