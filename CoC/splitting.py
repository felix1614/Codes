import re

ls = '*'
ss = '&'
p ="Roses are red*Violets are blue&Here's a new stanza*Just for you"
# print(p.replace(ls, '\n').replace(ss, '\n\n'))
# for i in p.split(ls):
#     if not re.search(ss,i):
#         print(i,end="\n")
#     else:
#         for j in i.split(ss):
#             print(j,end="\n")
n = 10
b=sum([i for i in range(n+1) if i%2==0])

# print(b)
I=input
I()
r=0
for i in I().split():
    r^=int(i)
    print(r^int(i))
I(r)



