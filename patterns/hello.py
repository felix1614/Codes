inputs = input().split()
w = inputs[0]
de = inputs[1]
o = int(inputs[2])
l=2+len(w)+o*2
for i in range(o):
    print(de*l)
print(de*o+" "+w+" "+de*o)
for i in range(o):
    print(de*l)