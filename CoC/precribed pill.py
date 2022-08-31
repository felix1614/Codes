"""
The target dose of an oral medication has been calculated d (in mg).

The only options to prescribe the medication are pills of strength a (in mg) and b (in mg), so it may not be possible to prescribe the exact target dose.

For a given target dose d, return the highest possible dose that can be made with any amount of pills a and/or b that does not exceed the target dose.
Input
Line 1: 3 space separated integers, d,a,b
representing the calculated target dose, the dose of pill a, and the dose of pill b (all in mg)
Output
Line 1: Integer value of the closest dose to the target that can be made without going above the target dose.
Constraints
a<=d
2<=d<=10000
1<=a<b<5000
Example
Input
91 25 60
Output
85

100 50 150      100

3640 225 425    3625

4540 9 15       4539
"""

d, a, b = [int(i) for i in input("Enter no: ").split()]
high = 0
for i in range(d):
    for j in range(d):
        if high <= (a * i)+(b * j) <= d:
            high = a*i+b*j
print(high)
