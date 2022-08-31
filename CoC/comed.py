'''A Japanese comedian once showed a joke that when you speak out a number which is a multiple of 3 or which contains the digit 3, it becomes dope. Let's try to implement it this time.

In the input, two integers are given. In the output, count up from the first integer to the second integer.
However, if the number is a multiple of 3 (3, 6, 9, 12, etc.), or if any digit has 3 in it (13, 23, 30, 31, etc.), output "Dope".
Input
An integer N1 to start counting up and an integer N2 to end counting up.
Output
The string to use when counting up. Put a "-" between each count.
Constraints
1 <= N1 <= 100000, 1 <= N2 <= 100000
N1 <= N2
Example
Input
1 5
Output
1-2-Dope-4-5'''
import itertools

n1=8
n2=20
# c=[]
# for i in range(n1,n2+1):
#     if "3" in str(i):
#         c.extend(["Dope","-"])
#     elif i%3!=0:
#         c.extend([str(i), "-"])
#     else:
#         c.extend(["Dope", "-"])
# print("".join(c[0:len(c)-1]))
# print(c)

s=list(itertools.chain(*[["Dope","-"] if "3" in str(i) else [str(i), "-"] if i%3!=0 else ["Dope", "-"] for i in range(n1,n2+1)]))
print("".join(s[0:len(s)-1]))
# print("".join(s[0:len(s)-1]))