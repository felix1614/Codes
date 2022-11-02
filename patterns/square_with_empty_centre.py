a=10
for i in range(a):
    for j in range(int(a)):
        if i==0 or i==a-1 or j==0 or j==a-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()