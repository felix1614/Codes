"""
The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01
Test 1
Input:  abbcccdddd
Expected output:    1a2b3c4d

02
Test 2
Input:  abcdefghijklmnopqrstuvwxyz
Expected output:
1a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z

03
Test 3
Input:  ZzzzzZzZZZzzzzzzzzzzzzzZZZZZZZZ
Expected output:
1Z4z1Z1z3Z13z8Z

04
Test 4
Input:  Hello
Expected output
1H1e2l1o

"""
# import itertools
s = input("Enter String: ")
c = 1
# e=[]
d = ""

for i in range(len(s)):
    if i < len(s)-1:
        if s[i] == s[i+1]:
            c += 1
        else:
            d += str(c)
            d += s[i]
            c = 1
    else:
        d += str(c)
        d += s[i]
print(d)
# print("".join(list(itertools.chain(*list(zip(d, e))))))





