# this file is to test the effect of average line strategy
# with different combinition

from broken_line import *
from strategy import *
import os

os.chdir('M:\\Python\\wealth management')

##def read_file(name):
##    try:
##        print('reading: '+str(name))
##        file = opne(str(name)+'.txt','r')
##        lines = file.realines()
##        file.close()
##        temp_line = broken_line()
##        for t in range(1,len(lines)-1):
##            if lines[t][0].isdigit():
##                temp = lines[t].split('\t')
##                temp_line.add_point(name,temp[0],float(temp[4]))
##        return temp_line
##    except:
##        return None

def read_file(name):
    try:
        print('reading: '+str(name))
        file = open(str(name)+'.txt','r')
        lines = file.readlines()
        file.close()
        temp_line = broken_line()
        for t in range(1,len(lines)-1):
            if lines[t][0].isdigit():
                temp = lines[t].split('\t')
                temp_line.add_point(name,temp[0],float(temp[4]))
        return temp_line
    except:
        return None



def analyze(line):
    # 273 day - 1 year
    length = line.length
    years = length/273
    first = line.points[0].value
    last = line.points[length-1].value
    #print(first,last,years)
    total_rate = (last-first)/first*100
    annual_rate = ((last/first)**(1/years)-1)*100
    temp_high = None
    for t in range(length):
        value = line.points[t].value
        if temp_high == None:
            temp_high = value
            temp_low = value
            temp_drop = 0
            continue
        if value < temp_high:
            temp_low = min(temp_low,value)
            temp_drop = max((temp_high-temp_low)/temp_high*100,temp_drop)#-%
        else:
            temp_high = value
            temp_low = value
    return total_rate, annual_rate, temp_drop
            
def main():
    period = [1,2,3,5,8,13,21,34,55]

    for t in range(5):
        short_period = period[t]
        for s in range(t+1,len(period)):
            long_period = period[s]

            file = open("strategy\\strategy_storage\\"+str(short_period)+\
            "_"+str(long_period)+"_average_strategy.txt","w")
            for num in range(1000):#

                closing_line = read_file('SH#'+str(num + 600000))
                average_strategy = strategy()
                average_strategy.short_period = short_period
                average_strategy.long_period = long_period
                
                if closing_line == None:
                    #print('here')
                    continue
                for i in range(closing_line.length):
                    average_strategy.update(closing_line.points[i])
                result_line = average_strategy.get_line()
                total_rate, annual_rate, temp_drop = analyze(result_line)

                file.write('SH#'+str(num + 600000)+'\ttotal: '+str(round(total_rate,2))+\
                           '%     annual: '+str(round(annual_rate,2))+'%     max drop: '+\
                           str(round(temp_drop,2))+'%\n')

            file.close()
            break
        break
            

main()
