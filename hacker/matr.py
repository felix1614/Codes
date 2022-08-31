def plusMinus(arr):
    a = [[], [], []]
    for i in arr:
        if i < 0:
            a[0].append(i)
        elif i > 0:
            a[1].append(i)
        else:
            a[2].append(i)

    print(len(a[0]) / len(arr))
    print(len(a[1]) / len(arr))
    print(len(a[2]) / len(arr))
plusMinus([-4,3,-9,0,4,1])