m, n = 1, 15
d = []
for i in range(m, n+1):
    c = format(int(i), "b")
    if c.count("0") % 2 == 0:
        d.append("1 ")
    else:
        d.append("0 ")
print("".join(d)[:-1])
