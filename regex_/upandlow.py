import re
d="aaf1@FABS"

a = "he4lo im kayak and i li2e in halo with my hellio"
# p="^i..m$"
# m = list(filter(None, list(map(lambda i: i if re.match(r"^[a-z]$|^([a-z]).*\1$", i) else None, a.split()))))
# m = list(filter(None, list(map(lambda i: i if re.match(r"^h.*o$", i) else None, a.split()))))
m = list(filter(None, list(map(lambda i: i if re.match('\d', i[round(len(i)/2)]) else None, a.split()))))
print(m)
# c = list(filter(None, list(map(lambda i: i if i[0] == 'h' and i[len(i)-1] == 'o' else None, a.split()))))
c = list(filter(None, list(map(lambda i: i if i[round(len(i)/2)].isdigit() else None, a.split()))))
print(c)

# if re.match(r"[a-z]|[A-Z]|\d|[!@#$%^&*?]",d) and re.match(r".+[!@#$%^&*?]|.+\d",d) and len(d)>=8:
if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",d):
    print('valid')
else:
    print('invalid')

