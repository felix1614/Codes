"""
The king wants to share his wealth with a certain number of people N in his kingdom, so he has provided a certain amount of gold coins A. Knowing that each person who receives gold coins wants twice as much as the person before him (and that the first person receives only one gold coin), has the king provided enough gold coins to give to the N people in his kingdom.

ex :

there are 3 people
the king has 15 gold coins

person 1 : 1 gold coin
person 2 : 2 gold coins
person 3 : 4 gold coins

--> 1+2+4 = 7 <= 15, the king has enough gold coins
Input
the number of people N to whom the king must give money
the number of gold coins A that the king has planned to give to his people
Output
True, if the king has enough gold coins to give to everyone N.
Otherwise, the number of people who received the gold coins they asked for.
Constraints
N is integer, 0<= N <= 1000
A is integer, 0<= A <= 1000000
Example
Input
3
15
Output
True

120
12000   13

12
4094    11

0
0       True

"""

n = 3
a = 15
c = []
for i in range(1, n+1):
    if len(c) == 0:
        c += i,
    else:
        c += c[i-2]*2,
if sum(c) <= a:
    print(True)
else:
    e = 0
    for i in c:
        if i <= a:
            e = c.index(i)
    print(e)
