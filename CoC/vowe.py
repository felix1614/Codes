sentence = "dashing rocseks aend claesh".lower().split(" ")
c=0
for i in range(len(sentence)):
    if i>0:
        c=0
    for j in sentence[i]:
        if j in "aeiou":
            c+=sentence[i].count(j)
    print(c)