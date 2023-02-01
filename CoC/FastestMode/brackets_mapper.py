"""

The goal is to know if the brackets is correct and return the opening/closing values of the brackets in a specific order.
Input
Line 1: a String openBracket that contains different types of open brackets and the order in which to print the number of their opening/closing brackets.
Line 2: a string closeBracket that contains different types of closing brackets and the order in which to print the number of their opening/closing brackets.
Line 3: a String message whose brackets must be checked.
Output
Line 1: true if the brackets are respected or false if they are not.
Line 2: the number of opening/closing brackets in the order of the brackets of the first entry or nothing if the brackets are not respected.
Constraints
1 ≤ length of openBracket ≤ 5
1 ≤ length of closeBracket ≤ 5
1 ≤ length of message ≤ 10000

Example
INPUT
{[(
}])
{[()]}
OUTPUT
true
1 1 1

INPUT
{[
}]
[{"text1":"QUOI ?","text2":["feur"], "text3":"bi"}]
OUTPUT
true
1 2

INPUT
{[(<
}])>
{{[<(>]}
OUTPUT
false

INPUT
{[
}]
[{"hello":["how","are","you"], "i\'m":[["fine"],["badly"}]}]
OUTPUT
false

"""

a = list(input())
b = list(input())
c = input()
ct = 0
l = []
for i, j in zip(a, b):
    l += str(c.count(i)),
    if c.count(i) != c.count(j):
        ct += 1
        break
if ct > 0:
    print("false")
else:
    print("true")
    print(" ".join(l))