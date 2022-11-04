import copy
import itertools


def sortt(arr):
    if len(arr) <= 1:
        return arr
    else:
        small, big = [], []
        piv = arr.pop()
        tuple(map(lambda x: small.append(x) if x < piv else big.append(x), arr))
        # for i in arr:
        #     if i < piv:
        #         small += i,
        #     else:
        #         big += i,
    return sortt(small) + [piv] + sortt(big)


arr = [[0, 9, 3, 8, 2, 5, 7, 5], [1, 4, 3, 7], [8, 6, 7]]
arrs = copy.deepcopy(arr)
output = list(map(sortt, arr))
outputOne = sortt(list(itertools.chain(*arrs)))
print(output)
print(outputOne)
