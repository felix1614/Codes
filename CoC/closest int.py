'''Given a positive integer N, print the smallest integer greater than N, such that none of its digits are in N.
Print "Impossible" if such a number doesn't exist.

Example :
Input: 12
Output: 30 -> ("12" doesn't contain "3" and "0")
Input
Line 1 : A positive integer N
Output
Line 1 : The next integer with different digits OR Impossible
Constraints
0 <= N <= 1234567890
Example
Input
36
Output
40'''


n = 36
c=n
d=True
if "".join(sorted(str(n)))!="0123456789":
    while d:
        if str(n).startswith(str(c)[0]):
            c+=1
        elif str(c)[0] in str(n):
            c += 1
        elif not str(n).startswith(str(c)[0]):
            d=False
    print(c)
else:
    print("Impossible")
# print(c)


