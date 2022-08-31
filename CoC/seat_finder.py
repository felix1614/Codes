"""

Help Jack Goff find a seat in classroom which is at equal distance from his friend Bob and crush Erica such that he's as near to them as possible.
It is guaranteed that a seat always exist in middle of Bob and Erica, as they are either sitting in the same row or same column or sitting diagonally to each other.
Input
The first line contains row and column number of Bob's seat: rb cb
The second line contains row and column number of Erica's seat: re ce
Output
Output the row and column number of Jack's seat: rj cj
Constraints
1≤ rb, cb, re, ce ≤ 10
Example
Input
1 3
3 1
Output
2 2
INPUT
9 10
1 2     5 6

INPUT
2 1
2 5     2 3

INPUT
3 1
5 3     4 2

"""
rb, cb = 2, 1
re, ce = 2, 5

b = int((rb+re)/2)
e = int((ce+cb)/2)
# print(b, e)

a=5
c=4
print(c)