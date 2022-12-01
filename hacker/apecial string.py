c = "abcbaba"
a = [i for i in c]
b = []
# indexes = [index for index, element in enumerate(a) if element == desired_element]
for j in range(len(a)):
    b.append(a[j])
    if j+2 < len(a)+1:
        if a[j] == a[j + 1]:
            b.append("".join(a[j:j + 2]))

        if len(a[j:j+3]) is 3 and a[j+2] == a[j]:
            b.append("".join(a[j:j+3]))
            a.append("")

        # if a[j+len(a)]==a[j] and a[j]==list(set(a[j+3]))[0]:
        # print(a[j:len(a)])
        # print(list(set(a[j:len(a)]))[0:len(a)-1])
        # print(set([i for i in a[j:j+4] if i.isalpha()]))
        # print(list(set([i for i in a[j:j+4] if i.isalpha()])))
        if len(a[j:j + 4]) is 4 and a[j] == list(set([i for i in a[j:j+4] if i.isalpha()]))[0] and a[j] == a[j:j+4][3]:
            # print(a[j:j + 4])
        # if a[j]==list(set(a[j:len(a)]))[0] and a[j]==list(set(a[j:len(a)]))[0:len(a)-1]:
        #     b.append("".join(a[j:len(a)]))
            b.append("".join(a[j:j+4]))
print(len(b), b)
# len(a[j:j+4]) is 4 and
# for i,e in enumerate(a):
#     if e==a[i]:
#         b.append((i,e))
# print(b)
# for i in a:
#     if a.count(i)>1:
#         if i not in b:
#             b.append(i)
#             # print(a[a.index(i)+2])
#
#             if a[a.index(i)]==a[a.index(i)+2]:
#                 print(a[a.index(i):a.index(i)+3])
#
# print(b)