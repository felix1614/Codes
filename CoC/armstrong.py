n = 407
temp = n
# sum = 0
#
# while n>0:
#     dig = n%10
#     sum += dig**3
#     n //=10
# if temp == sum:
#     print("arms", sum)
# else:
#     print("not a arms")


def arm(num):
    if num == 0:
        return num
    else:
        return pow((num%10), order)+arm(num//10)


order = len(str(n))
sum_ = arm(n)
if sum_ == int(n):
    print("arms", sum_)
else:
    print("not arms")