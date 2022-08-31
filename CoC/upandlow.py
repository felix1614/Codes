strn="aaaSaDCSa"
b=[i for i in strn]
c=0
d=[]
i=0
while i<len(b):
    if b[i].islower() and b[i+1].isupper() or b[i].isupper() and b[i+1].islower():
        b.remove(b[i])
        b.remove(b[i])
        c+=1
    elif b[i].isupper() and b[i+1].isupper() or b[i].islower() and b[i+1].islower():
        d.append(b[i])
        d.append(b[i+1])
        b.remove(b[i])
        b.remove(b[i])
        b.append('*')
    else:
        break
print("".join(d))
print(c)