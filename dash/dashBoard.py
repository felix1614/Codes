def quickSort(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq.pop()
        lower_arr, higher_arr = [], []
        tuple(map(lambda x: lower_arr.append(x) if x < pivot else higher_arr.append(x), seq))
    return quickSort(lower_arr) + [pivot] + quickSort(higher_arr)


arr = [4, 5, 7, 8, 2, 1, 10]
sortedArr = quickSort(arr)
print(sortedArr)
