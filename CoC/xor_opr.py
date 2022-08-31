a="001"
b="011"
print(bin(int(a,2)^int(b,2))[2:].zfill(len(a)))

ass="a"
c=0
for i in ass.lower():
    c+=ord(i)-96
print(c)