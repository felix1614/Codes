# sum_ = ''
# sam = ''
# for i in range(5):
#     row = input()
#     for j in row:
#         if row.count(j) > 1:
#             sum_ = '1'*(row.count(j))
#             sam = row[0]*(row.count(j))
# print(sum_+sam)
d = input("char")
c=list(map(lambda x: ("1"*(x.count(x)), x[0]*(x.count(x))) if x.count(x) >1 else "",d) for i in range(5))
for i in c:
    print(list(i))