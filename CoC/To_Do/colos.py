

s="+-+---"
c=0
for i in s:
    if i=='+':
        c+=1
    elif i=='-':
        c-=1
    elif i=='*':
        c*=5
    elif i=='/':
        c/=2
print(c)


