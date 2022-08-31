# height = 4
# width = 1
#
# for i in range(height):
#     print("O"*width)
a=1234
sum=0
for i in range(len(str(a))):
    if i<len(str(a)):
        sum+=int(i*int(str(a)[i+1]))
print(sum)