#mapper1:600031-600060
from General_Search import *
for n in range(600031,600060):
    try:
        file = open('SH#%s.txt'%(n),'r')
        file.close()
        cal_r(n)
    except:
        continue
