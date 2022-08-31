c = [-5, 1, 0]
d = (list(filter(lambda x: x is not None,set(list((map(lambda x: x if c.count(x) > 1 else None, c)))))))
print(d[0]) if len(d) >= 1 else print("no solution")

