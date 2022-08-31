import itertools
import os

from datetime import datetime
import apt_pro
# import apt

# d = os.system('dpkg -s slack')
pkg = 'slack'
# print(datetime.now())
c=[[],[["a","b"],[]],["c"]]
s=list(itertools.chain(*c))
df=list(itertools.chain(*s))
print(df)
# os.system(f'dpkg -s {pkg}')
# os.system(f'apt list | grep {pkg}')
# cache = apt_pro.Cache()
# cache.update()
# cache.open()
# pkg = cache[pkg]
# if pkg.is_installed():
#     print("is_installed")