'''Given an input string consisting of 2 distinct characters, output that string with each occurrence of one character replaced by the other.
Input
A single line, the input string.
Output
The string, with all occurrences of a character a replaced with the character b, and all occurrences of b replaced with a.
Constraints
2 ≤ string length ≤ 25
Example
Input
###*#***#*#
Output
***#*###*#*'''

s="###*#***#*#"
e=tuple(set(s))
print("".join([i.replace(e[0],e[1]) if i==e[0] else i.replace(e[1],e[0]) for i in s]))
# print(s)
