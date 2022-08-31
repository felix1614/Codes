n = int(input())
t = [int(i) for i in input().split()]
c = (print(f"{i} is here") if i in t else print(f"{i} is absent") for i in range(1, n+1))
for i in c: next(c)
