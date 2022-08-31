s_1 = "-6 8 5 -100 1024".split(" ")
s_2 = "0 1 5 100 64".split(" ")
c=[]
if len(s_1) == len(s_2):
    for i in s_1:
        if i.isdigit() or int(i):
            c += str(int(i)+int(s_2[s_1.index(i)])),
    print(" ".join(c))
else:
    print("Invalid")

