#mapper5:600231-600300
from General_Search import *
for n in range(600231,600300):
    try:
        file = open('SH#%s.txt'%(n),'r')
        file.close()
        cal_r(n)
    except:
        continue
