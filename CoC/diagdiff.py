import numpy as np
def diagonalDifference(arr):
    m=np.matrix(arr)
    # print(m.diagonal().sum())
    # print(np.matrix.diagonal(np.fliplr(m)).sum())

    return abs((m.diagonal().sum_()) - (np.matrix.diagonal(np.fliplr(m))).sum_())

if __name__ == '__main__':

    arr=[[1,2,3,4],[4,5,6,7],[7,8,9,10],[2,3,4,5]]
    result = diagonalDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
