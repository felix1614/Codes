n=1     #no.of cats
p=10    #time taken to give cat food
c=50    #waiting time for next cat
r=6     #giving name to a cat
t=0
for i in range(n):
    t+=p+(c+(((i+1)-1)*2))+r
print(t)
