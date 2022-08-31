c=4
d=3
e=[]
for i in range(d):
    row=input()
    for j in row:
        if j=='7':
            e.append(int(j))
print(sum(e))