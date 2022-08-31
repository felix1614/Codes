'''There are 3 numbers : d (day), m (month), y (year), forming a given date.
The application should output the numbers of days left till the end of the current year.
In case of non real date (ex. 29 days in non-leap year or 31 days in a 30 day month), application should return UKNOWN.
Input
Three inputs:
d : a given day
m : a given month
y : a given year
Output
One line number representing the number of days till the end of the year.
Constraints
0 < d <= 31
0 < m <= 12
0 < y <= 10000
Example
Input
28
10
6
Output
65

10
12
1550

22

31
12
1999

1

'''


d = int(input())
m = int(input())
y = int(input())

from datetime import date
from calendar import monthrange

# print(monthrange(y,m)[1])
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) and d == 29 and monthrange(y, m)[1] <= d:
    d1 = date(y, m, d)
    d2 = date(date(y, m, d).year, 12, 31)
    delt = d2-d1
    print(delt.days)
elif d <= monthrange(y, m)[1]:
    d1 = date(y, m, d)
    d2 = date(date(y, m, d).year, 12, 31)
    delt = d2 - d1
    print(delt.days)
else:
    print("UNKNOWN")
