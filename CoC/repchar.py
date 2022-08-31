l = "afnan";d=[]
tuple(map(lambda x:(d.append(l), print(l)) if x==0 else (d.append(f"{d[x-1][-1]}{d[x-1][0:-1]}"),print(d[x])) ,range(len(l)+1)))


# def lup():
#     l="codinggame";w=l
#     while True:
#         print(w);w=w[len(w)-1]+w[:-1]
#         if w==l:break
#     print(w)
# lup()
