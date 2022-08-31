'''The program:
Convert a string code of concatenated ASCII code numbers to the corresponding string of ASCII characters.

INPUT:
String of decimal numbers. Each number is 3 digits long and padded with zeroes.

OUTPUT:
The corresponding ASCII string.
If the input length is not a multiple of 3, then you should output the string ERROR.

CONSTRAINTS:
0 < Length of code ≤ 500
32 ≤ ASCII code ≤ 255

EXAMPLE:
Input
067111100105110103
Output
Coding '''


a = "067111100105110103"
if len(a) % 3 == 0:
    print("".join(list(map(lambda x: chr(int(x)), list(map(lambda i: a[i:i+3], range(0, len(a), 3)))))))
else:
    print("Error")




