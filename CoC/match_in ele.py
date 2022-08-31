"""
Given a string s, return the string with a space separating each group of consecutive identical characters. Case matters!

Example:
AAAABBBCCDAA --> AAAA BBB CC D AA
BbbAB --> B bb A B
Input
A string s
Output
The string with a space separating each group of consecutive identical characters.
Constraints
s contains only letters
|s| < 256
Example
Input
AAAABBBCCDAA
Output
AAAA BBB CC D AA

BbbABC      B bb A B C

ZZOOZZPPAAA     ZZ OO ZZ PP AAA

abcdefgh        a b c d e f g h

AaBbCcDDdEe     AaBbCcDDdEe
"""

s = "ZZOOZZPPAAA"
p = s[0]
tuple(map(lambda i: print(f'{i}', end='') if i is p else (print(f' {i}', end=''), p.replace(s, i)), s))


