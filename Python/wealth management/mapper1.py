#mapper1:600000-600030
from General_Search import *
for n in range(600000,600030):
    try:
        file = open('M:\\Python\\wealth management\\SH#%s.txt'%(n),'r')
        file.close()
        cal_r(n)
    except:
        continue
