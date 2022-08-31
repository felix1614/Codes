b,a=list(map(int,input("height, width: ").split()))
c,v,z=input(" Any 3 symbols: ").split()

for i in range(b):
    for j in range(a):
        if i==0 and j==0 or i==b-1 and j==a-1 or i==0 and j==a-1 or i==b-1 and j==0:
            print(z,end="")
        elif i==0 or i==b-1:
            print(c,end="")
        elif j==0 or j==a-1:
            print(v,end=" "*(a-2))
    print()
