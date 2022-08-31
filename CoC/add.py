n = int(input())
ch = input()
n1,n2=1,1
for i in range(n):
    print(ch*n1)
    c=n1+n2
    n1=n2
    n2=c

