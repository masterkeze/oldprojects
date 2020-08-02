#mapper4:600151-600230
from General_Search import *
for n in range(600151,600230):
    try:
        file = open('SH#%s.txt'%(n),'r')
        file.close()
        cal_r(n)
    except:
        continue
