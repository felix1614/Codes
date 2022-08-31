'''You are given a number sequence as such: 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, .. You need to find N-th number appearing in the sequence
Input
Single line: Number N, index of the number you need to find
Output
Single line: One integer representing N-th number in the sequence
Constraints
1<=n<=10¹⁴
Example
Input
3       55      13      51      1714636915      100000000000000
Output
2       10      3       6       29395           1749820
'''
import math

n=3
strt=int((math.sqrt(8*n+1)-1)/2)
remain=n-(strt*(strt+1)//2)
print([min(strt,remain),strt][remain==0])