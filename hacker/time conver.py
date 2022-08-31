import datetime

s="23:05"
# print(s[-2:])
if s[-2:] == "AM" :
    if s[:2] == '12':
          a = str('00' + s[2:8])
    else:
          a = s[:-2]
else:
    if s[:2] == '12':
          a = s[:-2]
    else:
          a = str(int(s[:2]) + 12) + s[2:8]
print(a)