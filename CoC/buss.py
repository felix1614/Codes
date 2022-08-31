n = int(input())
a=1
for i in range(n):
    get_in, get_off = [int(j) for j in input().split()]
    a+=get_in
    a-=get_off
print(a)