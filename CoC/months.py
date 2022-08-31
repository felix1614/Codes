# Given an ordered sequence of English months' first letter, output the next one.
#
# Ex: "JFM" => January, February, March => April => "A"
#
# There is always one and only one solution.
#
# A whole year is JFMAMJJASOND
# Input
# Line 1: months : a string of uppercase months' first letter
# Output
# Line 1: The first letter of the next month (uppercase)
# Constraints
# 1 ≤ length of months ≤ 100
# Example
# Input
# MAM
# Output
# J
# a="JFMAMJJASOND"
# months=input()
# for i in range(len(months)):
#     if i==len(months)-1 and months[len(months)-1]!='D':
#         # print(months.count(months[len(months)-1]))
#         print(a[a.index(months[i])+1])
#     elif i==a[len(months)-1]=='D':
#         print(a[0])
# if months[len(months)-1]!="D":
#     print(a[a.index(months[len(months)-1]) + 1])
# elif months[len(months)-1]=="D":
#     print(a[0])
# elif months.count(months[len(months)-1])>1:
#     print(a[])

m = input()
s = "JFMAMJJASOND"*9
print(s[s.find(m)+len(m)])



