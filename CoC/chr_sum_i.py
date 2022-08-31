"""
INput
1
LEET

OUT:
13


"""


n = int(input())
cd=[]
ef={'0':0,'i':1,'z':2,'e':3,'a':4,'s':5,'b':6,'t':7,'g':9}
for i in range(n):
    _str = input().lower()
    for j in _str:
        if j in ef:
            cd.append(int(ef.get(j)))
    print(sum(cd))
    cd.clear()
