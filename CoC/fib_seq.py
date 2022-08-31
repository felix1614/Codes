''' You must output the closest number in the Fibonacci Sequence to the number given. The Fibonacci Sequence is a series of numbers in which every number is equal to the sum of both numbers before it. The first numbers in the series are 1, 1. So the third is 2, and then 3, 5 etc.
Input
n, a natural number.
Output
dis, the distance of the closest number in the Fibonacci Sequence from n.
Constraints
1 ≤ n ≤ 1,000
Example
Input
6           64          233         1000
Output
1           9           0           13'''


num = 64
n1, n2 = 0, 1
s = [n1, n2]
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    if n3 <= num:
        s.append(n3)

print(s)
print(num-s[-1])
