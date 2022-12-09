def quick(seq) -> list:
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq.pop()
        data = {"min": [], "max": []}
        tuple(map(lambda x: data["min"].append(x) if x < pivot else data["max"].append(x), seq))
        return quick(data["min"]) + [pivot] + quick(data["max"])


def Binsearch(seq, low, high, ele):
    if len(seq) <= 1:
        return "invalid list"
    else:

        # leng = len(seq)
        # opt = int(leng/2)
        # if ele < seq[opt]:
        #     slicedSeq = seq[:opt]
        #     for i in range(len(slicedSeq)):
        #         if slicedSeq[i] == ele:
        #             return f"index: {i}, ele: {ele}"
        # else:
        #     slicedSeq = seq[opt:]
        #     for i in range(len(slicedSeq)):
        #         if slicedSeq[i] == ele:
        #             return f"index: {i+len(slicedSeq)}, ele: {ele}"
        if high >= low:
            mid = (high + low) // 2
            if seq[mid] == ele:
                return mid
            elif seq[mid] > ele:
                return Binsearch(seq, low, mid - 1, ele)
            else:
                return Binsearch(seq, mid + 1, high, ele)
        else:
            return -1


arr = [5, 4, 2, 1, 3, 10, 15, 12, 9, 8]     # array should be equal weighted
sortedArray = quick(arr)    # sorted array
print(sortedArray)
ele = int(input("Enter num: "))
print(f"Index of {ele} is {Binsearch(sortedArray, 0, len(arr)-1, ele)}")
