a=407
c=[]
for i in str(a):
    c.append(int(i)**3)
# print(c, sum(c))

print("armstrong number:",a) if a==sum(c) else print("not a armstrong number:",a)

number=54748
order = len(str(number))
sum_pow = 0
temp = number
while temp:
    temp, digit = divmod(temp, 10)
    sum_pow += digit ** order
print("arms:", number) if number == sum_pow else print("not arms:",number)


