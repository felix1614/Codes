# stri = "zApPeR"
# for i in range(len(stri)):
#     if (i+1) % 2 != 0:
#         if 65 <= ord(stri[i]) <= 90:
#             print(chr(ord(stri[i]) + 32), end="")
#         else:
#             print(chr(ord(stri[i]) - 32), end="")
#     else:
#         print(stri[i], end="")
#

# cds = 121
# if cds == cds[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

n = 121
temp = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev*10+dig
    n = n//10
if temp == rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
