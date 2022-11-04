def bubbleSort(seq):
    INDEX_LIMIT = len(seq) - 1
    sorted_ = False
    while not sorted_:
        sorted_ = True
        for i in range(INDEX_LIMIT):
            if seq[i] > seq[i+1]:
                sorted_ = False
                seq[i], seq[i+1] = seq[i+1], seq[i]
    return seq


# arrr = [[1, 4, 3, 2, 8, 6], [9, 0, 7, 8, 5]]
cd = bubbleSort([2, 5, 1, 3, 6, 3, 0])
print(cd)
# ef = list(map(bubbleSort, arrr))
# print(ef)

