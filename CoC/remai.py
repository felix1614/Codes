a = 5
b = 6
if a > 1:
    for i in range(2, a):
        if (a % i) == 0:
            print(a, "is not a prime aber")
            break
    else:
        print(a, "is a prime aber")
else:
    print(a, "is not a prime aber")
