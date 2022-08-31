d=28
g,e,a=250,20,20
for i in range(d):
    g-=e
    g+=a
if g<=0:
    print('Dead')
else:
    print(g)