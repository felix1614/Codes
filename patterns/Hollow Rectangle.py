n = 11
for i in range(int(n/2)):
    for j in range(n):
        if i == 0 or i == int(n/2)-1 or j == 0 or j == n-1:
            print("*", end=" ")
        elif i == int((int(n/2))/2) or j == int(n/2) or i in [1, int((int(n/2))/2)+1] and j in [1, n-2]:
            print("@", end=" ")
        else:
            print(" ", end=" ")
    print()
