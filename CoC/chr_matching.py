length = int(input())
A = [[], []]
for i in input().split():
    A[0] += i,
for i in input().split():
    A[1] += i,

c = []
for i in A[0]:
    if i in A[1] and i not in c:
        print(A[1].index(i))
        c += i,
    else:
        print('NONE')
