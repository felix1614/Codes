s = int(input())
d = int(input())
n = int(input())
r = input()

if s == d:
    print("Already There")

elif (int("".join(set(map(lambda x: str(r.find(str(d))) if str(d) in r else "", r))))) * 10 <= n:
    print("Arrive")
else:
    print("Won't Arrive")
