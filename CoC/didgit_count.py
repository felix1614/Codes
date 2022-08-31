"""
Given a string input you must divide the number of letters in that string by the number of digits in that string. Round the resulting number to the nearest integer.
Input
One string input, containing only ASCII characters.
Output
One integer, representing the letter count divided by the digit count of input.
Constraints
2 <= length of input <= 256
There is always at least one digit in input
Example
Input
He110 W0r1d!
Output
1

1f u didn't underst4nd0         5
1 c4n't he1p                    2
S0, 1f u turn 0n u'r br4in u wi11 underst4nd            4
L00k at symb01s                 2
Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1e Ex4mp1                      2
g0 G0 g0 G0 gGgG0000            1
L=1                             1
a=4,o=0,z=2                     1
"""

inp = input()
c, d = 0, 0
for i in inp:
    if i.isdigit():
        c += 1
    elif i.isalpha():
        d += 1

print(abs(round(d/c)))

