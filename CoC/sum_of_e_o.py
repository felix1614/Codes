a=[0,0]
# map(lambda x: a[0].append(int(x)) if int(x)%2==0 else a[1].append(int(x)),input().split(" "))
for i in input().split():
    if int(i)%2==0:
        a[0]+=int(i)
    else:
        a[1]+=int(i)

print(a[1]-a[0])