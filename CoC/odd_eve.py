d = list(map(lambda x: input("enter: "), range(int(input("enter qty: ")))))

print("\n".join(list(map(lambda x: d[(x*2) % len(d)], range(len(d)//2)))))
print("\n".join(list(map(lambda x: d[(x*2+1) % len(d)], range(len(d)//2)))))
