candles_count = int(input().strip())

a = list(map(int, input().rstrip().split()))
b=max(a)
print(b)
print(a.count(b))