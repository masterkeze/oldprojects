#mapper3:600090-600150
from General_Search import *
for n in range(600090,600150):
    try:
        file = open('SH#%s.txt'%(n),'r')
        file.close()
        cal_r(n)
    except:
        continue
