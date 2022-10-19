n = 5005
# temp = n
# rev = 0
#
# while n > 0:
#     dig = n % 10
#     rev = rev*10+dig
#     n //= 10
# if temp == rev:
#     print("palindrome:", rev)
# else:
#     print("not palindrome", rev)


def pal(num, temp):
    if num == 0:
        return temp
    temp = (temp*10)+(num % 10)
    return pal(num//10, temp)


temp =pal(n, 0)
if temp == n:
    print("palindrome:", temp)
else:
    print("not palindrome")