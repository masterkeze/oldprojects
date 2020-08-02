from Data_Calculator import *
file = open('SH#600000(compare).txt','w')
file.write('Correlation of SH#600000\n')
topten = list()
lastten = list()
for i in range(600001,604000):
    try:
        r = getr('SH#600000','SH#%s'%(i))
        output = 'SH#%s: '%(i)+str(r)+'\n'
        file.write(output)
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
print(topten)
print(lastten)
