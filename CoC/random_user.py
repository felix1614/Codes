import random
char = 10
n = 3
c=["Word","Simple","Example"]
d=(["".join(random.choices(c,k=char)) for i in range(n)])
print(d)
# print(list(map(lambda i: d[i:i+3], range(0, len(d), 10))))
print(len(d))