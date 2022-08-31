# A number n is good if it can be written as the sum of at least two positive integers such that the sum of their inverse is equal to 1. Moreover, if all the numbers in the decomposition are equal, we say that the number is really good
# Otherwise, we say that the number is bad.
#
# For example :
# 2 is bad because the only way we can decompose 2 is 2=1+1 and 1/1+1/1=2 which is not equal to 1.
# 4 is a really good number because 4=2+2 and 1/2+1/2=1 (2 is the only number used in the decomposition).
# 10 is a good number because 10=4+4+2 and 1/4+1/4+1/2=1 (2 and 4 are both used in the decomposition).
#
# Given an integer n output really good if it's a really good number, good if it's a good number, bad otherwise.

n=4
arr=[]
c=[]
def print_v(arr):
    if (len(arr) != 1):
        d=[]
        for i in range(len(arr)):
            # print(arr[i], end=" ")
            d.append(i)
        # c.append(d)
        c.append(d)
        d.clear()
    # print(c)
def find_(arr,i,n):
    if n==0:
        print_v(arr)
    for j in range(i,n+1):
        arr.append(j)
        find_(arr,j,n-j)
        del arr[-1]
    # print(arr)
find_(arr,1,n)

