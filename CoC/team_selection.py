"""
There are too many applicants for a talent show. To select the best ones, groups are formed and each participant of a group is evaluated. The participant with the most points of the group is selected.

If several participants have the most points, all of them are selected.

You are given N groups with P participants each, as well as the number of points each participatant has scored.

How many participants will be selected and how many points they score in total?
Input
Line 1: An integer N for the number of groups.
Line 2: An integer P for the number of participants in a group.
Next N lines: A line of P integers representing the points scored by each participant of this group, separated by spaces.
Output
Two integers representing the number of selected participants and the sum of their points, separated by a space.
Constraints
2 ≤ N, P ≤ 15
0 ≤ points ≤ 9
Example
Input
3
4
2 0 0 5
5 7 4 6
1 8 5 4
Output
3 20

4
5
5 2 7 3 9
3 0 6 2 7
1 6 3 8 2
9 0 0 1 3           4 33

2
6
1 5 5 8 8 4
9 9 5 9 9 5         6 52

15
15
0 2 3 7 8 7 2 9 5 0 2 2 5 5 9
8 9 4 9 5 0 4 8 6 9 0 7 4 3 9
1 3 0 4 7 4 0 2 1 3 5 0 7 1 5
3 1 0 2 6 9 1 9 2 8 6 1 9 0 1
9 9 0 4 9 6 6 6 6 8 3 9 6 6 1
4 6 9 5 2 9 5 6 4 2 9 7 7 3 2
7 8 2 1 4 3 6 5 4 9 1 1 8 2 8
9 4 7 9 3 7 7 2 9 4 6 1 8 3 0
7 0 2 8 2 1 0 2 6 5 4 5 7 7 4
7 0 3 2 2 1 7 5 6 1 0 8 9 5 8
5 9 6 4 4 1 9 0 5 1 8 4 5 8 3
2 2 9 3 8 7 7 3 0 2 9 6 8 3 3
3 0 1 8 4 8 3 5 7 8 3 2 5 6 0
0 3 6 7 0 2 5 4 3 7 3 3 5 8 3
3 9 4 5 5 1 8 4 8 6 8 8 1 9 3       34 297

8
8
4 5 0 5 4 1 8 3
2 7 3 1 1 7 1 8
8 6 6 2 9 6 9 2
2 9 9 8 9 3 6 5
5 3 1 0 7 3 9 6
2 7 8 3 0 5 7 2
2 4 5 0 9 7 4 8
3 4 0 8 6 6 9 5             11 96
"""

# n=3
# p=4
# for i in range(n):
#     c=sorted(list(map(int,input().split())))

i, I = int, input
n = i(I("enter:"))
p = i(I())
a, b = 0, 0
for _ in range(n):
    *q, = map(i, I().split())
    u = max(q); t = q.count(u)
    a += t
    b += t*u
print(a, b)

