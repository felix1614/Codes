n=12
rev=0
while n!=0:
    rev=rev*10+n%10
    n=(n//10)
print(rev)

na=12345
print(int(str(na)[::-1]))