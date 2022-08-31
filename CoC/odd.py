# import re
# import sys
# import math
#
# # Auto-generated code below aims at helping you parse
# # the standard input according to the problem statement.
# #
# # sentence ="h1ll0 jhgw123jh"
# # b=[int(i) for i in sentence.lower() if ord(i)>=49 and ord(i)<=57]
# # print(sum(b))
# #
# # b=[]
# # print(sentence.lower())
# # print(ord('9'))
# # for i in sentence.lower():
# #     if ord(i)>=49 and ord(i)<=57:
# #         b.append(int(i))
# # print(sum(b))
# su=[]
# sa=[]
# as_="hekl12 bh2 87 hjb2223kjh"
# # for i in as_.split():
# #     if i.isdigit():
# #         su.append(int(i))
# #     else:
# #         for j in i:
# #             if j.isdigit():
# #                 sa.append(int(j))
# # print(sum(su)+sum(sa))
# ac=sum([int(i) if i.isdigit() else sum(list(map(lambda x: int(x) if x.isdigit() else 0,i))) for i in as_.split()])
# print(ac)
# a="ABC"
# b=[]
# for i in range(len(a)):
#     b.append(ord(a[i])*i)
# print(b)
# print(sum(b))
# a=sum(ord(a[i])*i for i in range(len(a)))
# print(a)


# b=[]
# for i in range(len(as_)):
#     if ord(as_[i])<49 or ord(as_[i])>57:
#         b.append(" ")
#     elif ord(as_[i]) >= 49 and ord(as_[i]) <= 57:
#         b.append(as_[i])
# c=[]
# for i in "".join(b).split(" "):
#     if i !="":
#         c.append(int(i))
# print(sum(c))


# if ord(as_[i])>=49 and ord(as_[i])<=57:
#     pass

# for iin as_.split((re.findall('',as_)))
# w="ABC"
# for i in range(int(input())): print(w)
a = 3210
# b = []
# for i in str(a):
#     if int(i) != 0:
#         b.append(str(int(i) - 1))
# print(int("".join(b)))
b=['ab','bb',')-_*(',')*..*(']
for i in b:
    print("".join(i[::-1]))
# print(str(b.reverse()) for i in b[::-1])