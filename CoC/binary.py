"""

Find the digit at the given index in the sequence of concatenated binary natural numbers.

The binary sequence starts with 0=0, 1=1, 10=2, 11=3, 100=4, 101=5, 110=6, 111=7, 1000=8, 1001=9, ...
Putting it all together it gives
01101110010111011110001001...
| |   |   |

Indexes are given in binary (zero based).
So for example, the digit at indexes 0=0, 10=2, 110=6 and 1010=10 (the ones marked) are 0, 1, 1 and 0.
Input
Line 1: An integer N for the number of indexes.
Next N lines: The binary integer of each index.
Output
N lines: The digit (0 or 1) present at the corresponding index
Constraints
1 ≤ N ≤ 20
0 ≤ index < 2^10
Example
Input
4
0
1
10
11
Output
0
1
1
0

4
1101    1
1001    1
0101    1
0010    1

20
1000111100  1
1001100000  0
1111010000  0
1111110011  0
1001010001  1
1100010000  0
1100011001  0
1000000001  1
1011000000  1
1101011011  0
1001011010  1
1111010101  1
1011100011  0
1111010110  1
1101100001  1
1111011100  0
1100110001  1
1011111100  1
1110111101  1
1100101101  0
"""
import re

c="001"
