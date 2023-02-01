class Fib:
    def __init__(self):
        self.first = 0
        self.sec = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.first
        self.first, self.sec = self.sec, self.first + self.sec
        return result


fib = Fib()
for i in range(10):
    print(next(fib))
    #


def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


fibb = fibo()
print([next(fibb) for i in range(10)])
