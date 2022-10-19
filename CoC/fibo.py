n_=10


def fib(n):
    a=0
    b=1
    if n < 0:
        print("incorrect inp")
    elif n==0:
        print(n)
    elif n==1:
        print(b)
    else:
        for i in range(1, n):
            c = a+b
            a = b
            b = c
        return b

# print(fib(n_))


# recursion
def fibo(n):
    if n < 0:
        print("incorrect inp")
    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


print(fibo(n_))






