arr=[1,2,3,4,5]
c=[[],[],[]]
for i in range(len(arr)):
    c[0].append(arr[i+1:])
    c[1].append(arr[:i+1])
for j in range(len(c[1])):
    if j==0:
        c[2].append(sum(c[0][j]))
    else:
        c[1][j].pop(len(c[1][j])-1)
        c[0][j].extend(c[1][j])
        c[2].append(sum(c[0][j]))
print(min(c[2]),max(c[2]))