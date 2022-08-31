# Given a list of W words, concatenate them together to form an NxN grid and return the two words on the main diagonals (top to bottom) in alphabetical order.
# Input
# Line 1: The size N of the grid and word.
# Next W lines: The word list.
# Output
# One line with the two diagonal words, space separated and in alphabetical order.
# Constraints
# 3 ≤ N ≤ 20
# W ≤ 100
# Example
# test case ==>1
# Input
# 3
# cow
# bat
# rat

# Output
# cat war


#test case ==>2
# 5
# 5
# sack
# cute
# harbour
# skull
# elite

#output
#choke stole

#test case ==>3
# 8
# 10
# magical
# academy
# bail
# reasoning
# golden
# alliance
# auto
# negotiate
# alert
# angel

#output
#absolute marginal

x=int(input("Enter no: "))
row ="".join([input() for i in range(x)]) #alpha_input
while len(row)!=x*x:
    print("row char should be equal to the multiple of x")
    row="".join([input() for i in range(x)])
res=[row[y-x:y] for y in range(x, len(row)+x,x)]
d=[[res[i][i] for i in range(len(res))],[res[len(res) - 1 - j][j] for j in range(len(res))]]
print(("".join(d[0])),("".join(d[1][::-1]))) if d[0][0]<d[1][0] else print( ("".join(d[1][::-1])),("".join(d[0])))

