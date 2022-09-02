"""
As Logan's 4 year-old daughter is new to maths, she has trouble understanding sums when they are given in a string with numbers in an arbitrary order, such as 3+5+2.
Therefore, her father will help her to understand sums by arranging the numbers of each string sum in ascending order, such as 2+3+5.

Your job is to help Logan arrange the numbers in ascending order and print the sum in a form that his daughter can understand.
Input
Line 1 : the string sum.
Output
A string containing the sum described in sum with each number in ascending order.
Constraints
sum contains only digits and the + character.
None of the numbers of sum are negative.
Every number of sum has a single digit.
sum is at most 100 characters long.
Example
Input

1+3+2

Output

1+2+3
"""

print('+'.join(sorted(input().split('+'))))
