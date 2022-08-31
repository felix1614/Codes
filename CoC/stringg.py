sent="this is crazy and fun"
list=["is","fun"]
b=[i.capitalize() if i not in list else i for i in sent.split(" ") ]
print(" ".join(b))
# for i in sent.split(" "):
#     if i not in list:
#         b.append(i.capitalize())
#     else:
#         b.append(i)
# print(" ".join(b))
a1=[1,2,3,4,5,]
a2=[4,5,6,7,8,9]
a3=[7,8,9,10,12]
a1.extend(a2)
a1.extend(a3)

# print(sorted(a1))
print(sorted(set(a1)))
print(max((sorted(set(a1)))[:-4]))
