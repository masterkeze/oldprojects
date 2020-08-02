import os
import pickle
os.chdir('M:\\Python\\wealth management')
#Statistics
def avg(data):
    return sum(data)/len(data)

def sstd(data):
    avg = sum(data)/len(data)
    vol = 0
    for n in data:
        vol += (n-avg)**2
    sstd = (vol/(len(data)-1))**0.5
    return sstd

def std(data):
    avg = sum(data)/len(data)
    vol = 0
    for n in data:
        vol += (n-avg)**2
    std = (vol/len(data))**0.5
    return std

def correlation(x,y):
    lx = len(x)
    ly = len(y)
    if lx <= ly:
        n = lx
    else:
        n = ly
    stdx = std(x)
    stdy = std(y)
    temp = 0
    for i in range(n):
        temp += (x[i]-avg(x))*(y[i]-avg(y))
    stdxy = temp/n
    r = stdxy/(stdx*stdy)
    return r
    
#Calculation
def getdata(name,index):
    try:
        file = open('M:\\Python\\wealth management\\quick_save\\'+str(name)+'.pkl','rb')
        data = pickle.load(file)
        file.close()
        output = data[index]
    except:
        file = open('M:\\Python\\wealth management\\'+str(name)+'.txt','r')
        lines = file.readlines()
        file.close()
        data = list()
        for temp in range(7):
            data.append([])
        for i in range(2,len(lines)-1):
            line = lines[i].split('\t')
            #print(line)
            for j in range(len(line)):
                data[j].append(line[j])
        file = open('M:\\Python\\wealth management\\quick_save\\'+str(name)+'.pkl','wb')
        pickle.dump(data,file)
        file.close()
        print('New file created:'+name+'.pkl')
        output = data[index]
    return output

def getreturn(name):
    data = getdata(name,4)
    output = list()
    length = len(data)
    for i in range(length-1):
        temp = (eval(data[i+1])-eval(data[i]))/eval(data[i])
        temp = round(temp,5)
        output.append(temp)
    return output

def getsstd(name):
    data = getreturn(name)
    output = sstd(data)
    return output

def getstd(name):
    data = getreturn(name)
    output = std(data)
    return output

def getr(name1,name2):
    data1 = getreturn(name1)
    data2 = getreturn(name2)
    return correlation(data1,data2)
