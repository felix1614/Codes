a="FrFbLfF"
b=[0,0]
d=[sum([b[1]+1 if i is "F" else b[1]-1 if i is "B" else 0 for i in a.upper()]), sum([b[0]+1 if i is "R" else b[0]-1 if i is "L" else 0 for i in a.upper()])]
print(d[1],d[0])
# c=[0,0]
# for i in a.split(" "):
#     if i=="F":
#         c[1]+=1
#     elif i=="B":
#         c[1]-=1
#     elif i=="R":
#         c[0]+=1
#     elif i=="L":
#         c[0]-=1
#
# print(c[0],c[1])