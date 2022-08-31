# print(sum([int(i) for i in str(int(input("1: "))**int(input("2: ")))]))
print(sum(list(map(lambda x: int(x), str(int(input("1: "))**int(input("2: ")))))))
# n_1, n_2 = input().split()
#
# print(n_1 or n_2)

# inp 1:45
# inp 2:34
# out: 261

# inp1:3
# inp2:4
# out:9

# inp1: 6
#inp2: 10
# print(3**4)
# out: 36
# c=0
# for i in str(6**10):
#     c+=int(i)
# print(c)