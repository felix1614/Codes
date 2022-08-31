# sum of the diagonals
# inp_1=4 inp_2=1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
'''    1 2 3 4
       5 6 7 8
       9 0 1 2
       3 4 5 6 '''

#out=19

import numpy as np
n = int(input("Array_size: "))
value = np.array_split([int(input(f"{i}: ")) for i in range(0, n*n)], n)
c = sum([sum(value[j])-value[j][0] if j == 0 else 0 if j == len(value)-1 else value[j][len(value)-1] for j in range(len(value))])
print(c)

# for i in range(len(value)):
#     if i==0:
#         c.append(sum(value[i])-value[i][0])
#     elif i==len(value)-1:
#         continue
#     else:
#         c.append(value[i][len(value)-1])
# print(sum(c))
