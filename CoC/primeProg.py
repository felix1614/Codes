start = 1
end = 10

# from start to end
# for i in range(start, end+1):
#     if i > 1:
#         for j in range(2, i):
#             if (i % j) == 0:
#                 break
#         else:
#             print(i)
#
# # prime no using loop
# n = 11
# if n > 1:
#     for i in range(2, int(n/2)+1):
#         if (n % i) == 0:
#             print(n, "is not a prime number")
#             break
#     else:
#         print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")


# prime no using recursion
def primeNo(n, i=2):
    if n == i:
        return True
    elif n % i == 0:
        return False
    return primeNo(n, i+1)



n = 1
if n > 1:
    if primeNo(n):
        print(n, "is primeNo")
    else:
        print(n, "is not primeNo")
else:
    print(n, "is not a prime number")
