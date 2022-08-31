from datetime import datetime
from dateutil.relativedelta import relativedelta
d=0
c=[]
for year in range(5):
    c += (datetime.now() - relativedelta(years=d)).strftime("%Y"),
    if d >= 3:
        d -= 4
    else:
        d += 1
print(sorted(c))