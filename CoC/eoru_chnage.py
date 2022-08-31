"""You are given the set of whole euro bills and coins:
€500, €200, €100, €50, €20, €10, €5, €2, €1
and an integer sum.
Your task is to find out how to pay the sum with the least number of coins/bills. For each bill/coin in the euro set, print the number of times you need this bill/coin on its own line.
Input
Line 1: an integer sum.
Output
Line 1: the number of €500 bills needed.
Line 2: the number of €200 bills needed.
Line 3: the number of €100 bills needed.
Line 4: the number of €50 bills needed.
Line 5: the number of €20 bills needed.
Line 6: the number of €10 bills needed.
Line 7: the number of €5 bills needed.
Line 8: the number of €2 coins needed.
Line 9: the number of €1 coins needed.
Constraints
0 ≤ sum ≤ 2^31-1.
Example
Input
123
Output
0
0
1
0
1
0
0
1
1"""
from datetime import datetime

_sum = 999
bills = [500, 200, 100, 50, 20, 10, 5, 2, 1]
for i in bills:
    if _sum // i == 0:
        print(0)
    else:
        n = _sum//i
        print(n)
        _sum -= n*i


