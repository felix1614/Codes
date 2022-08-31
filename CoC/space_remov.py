l = "CODINGAME!"
c=[]
for i in l:
    if not i.isalpha():
        c.append(f"{i}")
    elif i.isalpha():
        c.append(f"{i}")
        c.append(" ")
if not c[(len(c)-1)].isalpha():
    if c[(len(c) - 1)] == " ":
        c.pop(len(c)-1)
    elif not c[(len(c) - 1)].isalpha():
        c.pop(len(c)-2)

    # else:
    #     c.append(f"{i}")
print("".join(c))