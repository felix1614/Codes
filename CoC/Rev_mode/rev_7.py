s = "pglnhenftjdscs pmdchawvngmckde"
# print("".join(tuple(map(lambda x: s[x], range(2, len(s), 3)))))

n=3
a=15
c=[]
for i in range(1,n+1):
    if len(c)==0:
        c+=i,
    else:
        c+=c[i-2]*2,
if sum(c)==a:
    print(True)
else:
    print(False)