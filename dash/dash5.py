fact = lambda x: x if x == 1 else x * fact(x - 1)
print(fact(6))  # factorial

is_prime = lambda num: num > 1 and all(num % i for i in range(2, num))
print(is_prime(5))  # prime

fib = lambda fibo: fibo if fibo <= 1 else fib(fibo-1) + fib(fibo-2)
n = 5
print(list(map(fib, range(n))))  # fibonacci

df = [f"gateway_type_{type}" for type in range(1, 10) if type != 7]
print(df, end="\n")



