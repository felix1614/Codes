"""There is a total of n trains going from station A to station B say d km distance. Each train has a different speed s
measured in km/hr and a unique number tun.
Every train stops at p different stations, at every station between A and B the train has to wait for 30 minutes.

You have to reach station B as fast as possible for your interview at Google, Select your train.
Input
Line 1: An integer d for the distance between station A and station B in km.
Line 2: An integer n for the total amount of trains available.
Next n lines : A float s for the speed of the train measured in km/hr, An integer tun for the train's unique number, and
 a float p for the amount of stations between station A and station B all separated by a space.
Output
The unique number of the first train to reach station B
Constraints
1000 >= d >= 100
8 > n >= 2
200 >= s >= 80
50 >= p >= 2
tun is always made of 5 digits
Example
Input
200
3
120 12230 3
160 23440 2
180 33250 7
Output
23440

160
4
90 25667 2
120 46732 4
200 22674 3
180 77263 5
output
22674

130
2
109 33567 3
110 44567 2
output
44567

670
6
120 22783 2
160 33678 3
200 27763 2
80 33678 4
180 44678 5
190 22982 3
output
27763"""

# d = 200
# n = 3
# c = [[], []]
# for i in range(n):
#     inputs = input().split()
#     c[0].append(d/(float(inputs[0])/float(inputs[2])))
#     c[1].append(inputs[1])
# print(c[1][c[0].index(min(c[0]))])

n = int(input())
d=[]
for i in range(n):
    d.append(int(input()))
e=d.sort(reverse=True)
print("".join(str(d))[1:-1].replace(',', ' '))

