import array
import queue

"""
    u ==> Unicode char
    b ==> Signed char
    B ==> Unsigned char
    h ==> Signed short
    H ==> Unsigned short
    l ==> Signed long
    L ==> Unsigned long
    q ==> Signed Long long
    Q ==> Unsigned Long long
    f ==> float
    d ==> double
    i ==> Signed int
    I ==> Unsigned int
"""
arr = array.array('d', [2.5, 6.0, 7.1])
print(arr)
arr[0]=60
arr.append(5)
print(arr)
print(arr.count(10))
arr.insert(1,3)
print(arr)
