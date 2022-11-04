"""
Faster compared to Bubble Sort and selection sort
"""


def insertSort(list_a):
    index_length = range(1, len(list_a))
    for i in index_length:
        valueToSort = list_a[i]

        while list_a[i-1] > valueToSort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i -= 1
    return list_a


# arr = [2, 1, 5, 6, 3, 4, 5]
arr = [2, 35, 6, 1, 6, 3]
print(insertSort(arr))