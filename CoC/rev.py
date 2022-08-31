
s = "butter exile".split(" ")
c=""
for i in s:
    c+=i[0]
for j in s[::-1]:
    c+=j[-1]
print(c)