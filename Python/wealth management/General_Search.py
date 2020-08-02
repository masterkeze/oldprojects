from Data_Calculator_1_1 import *
import time
def cal_r(n):#SH
    time1 = time.time()
    file = open('M:\\Python\\wealth management\\SH#%s(compare).txt'%(n),'w')
    file.write('Correlation of SH#%s\n'%(n))
    topten = list()
    lastten = list()
    for i in range(n+1,604000):
        try:
            r = getr('SH#%s'%(n),'SH#%s'%(i))
            output = 'SH#%s: '%(i)+str(r)+'\n'
            #file.write(output)
            if len(topten)<10:
                temp = [r,'SH#%s'%(i)]
                topten.append(temp)
                topten.sort()
                topten.reverse()
            else:
                if r>topten[9][0]:
                    temp = [r,'SH#%s'%(i)]
                    topten[9] = temp
                    topten.sort()
                    topten.reverse()
            if len(lastten)<10:
                temp = [r,'SH#%s'%(i)]
                lastten.append(temp)
                lastten.sort()
            else:
                if r<lastten[9][0]:
                    temp = [r,'SH#%s'%(i)]
                    lastten[9] = temp
                    lastten.sort()
        except:
            continue
    file.write('\tThe top ten:\n')
    for i in range(10):
        output = topten[i][1]+': '+str(topten[i][0])+'\n'
        file.write(output)
    file.write('\tThe last ten:\n')
    for j in range(10):
        output = lastten[j][1]+': '+str(lastten[j][0])+'\n'
        file.write(output)
    file.close()
    time2 = time.time()
    print('SH#%s(compare).txt Done. Time Cosuming: %s'%(n,time2-time1))

def main():
    for n in range(601000,603000):
        try:
            file = open('SH#%s.txt'%(n),'r')
            file.close()
            cal_r(n)
        except:
            continue

