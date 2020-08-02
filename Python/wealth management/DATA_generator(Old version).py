import os
from math import sqrt
os.chdir('M:\\Python\\wealth management')
global data
global title

def reverse(stock_index):
    global title
    file = open('%s.txt'%(stock_index),'r')
    lines = file.readlines()
    file.close()
    rfile = open('%s(sta).txt'%(stock_index),'w')
    rfile.write(lines[0])
    lines.reverse()
    for i in range(len(lines)-1):
        rfile.write(lines[i])
    rfile.close()

def read(stock_index):
    global data
    global title
    file = open('%s(sta).txt'%(stock_index),'r')
    lines = file.readlines()
    data = list()
    for line in lines:
        if line:
            #print(line,end='')
            line = remove_comma(line)
            if lines[0] == line:
                title = line[:len(line)-1].split('\t')
##                for index in range(len(title)):
##                    title[index] = str(index)+title[index]
            else:
                temp = line[:len(line)-1].split('\t')
                data.append(temp)
    file.close()

def remove_comma(string):
    #print(string)
    i = 0
    while i < len(string):
        if string[i] == ',':
            string = string[:i]+string[i+1:]
            continue
        i = i + 1
    return string

def getdata(index):
    'index:1-开盘价, 2-最高价, 3-最低价, 4-收盘价, 5-成交量, 6-涨跌幅 '
    duration = len(data)
    start_date = data[0][0]
    end_date = data[duration-1][0]
    output = list()
    for eachday in data:
        output.append(eachday[index])
    #print('Date from '+start_date+' to '+end_date)
    return output

def rewrite(stock_index):
    global title
    file = open('%s(sta).txt'%(stock_index),'w')
    for title_name in title:
        file.write(title_name)
        if title_name == title[len(title)-1]:
            file.write('\n')
        else:
            file.write('\t')

    for each_day in data:
        for content in each_day:
            file.write(content)
            if content == each_day[len(each_day)-1]:
                file.write('\n')
            else:
                file.write('\t')
    file.close()
    return

def getreturn(stock_index):
    global data
    global title
    title.append('涨跌幅')
    price_list = getdata(4)
    pointer = 1
    data[0].append('None')
    output = list()
    while pointer < len(price_list):
        temp = (eval(price_list[pointer])-eval(price_list[pointer-1]))/eval(price_list[pointer-1])
        output.append(temp)
        temp = round(temp,4)
        data[pointer].append(str(temp))
        pointer = pointer + 1
    rewrite(stock_index)
    return output

def getstd(stock_index):
    global title
    global data
    title.append('样本std')
    list1 = getdata(6)
    list2 = list()
    for i in list1:
        list2.append(eval(i))
    list2.remove(None)
    _x = sum(list2)/len(list2)
    vol = 0
    for num in list2:
        vol+=(num-_x)**2
    vol = vol/(len(list2)-1)
    std = sqrt(vol)
    std = round(std,5)
    data[0].append(str(std))
    for i in range(1,len(list1)):
        data[i].append('None')
    rewrite(stock_index)
    return std

def main(stock_index):
    reverse(stock_index) 
    read(stock_index)
    getreturn(stock_index)
    getstd(stock_index)

main(300416)
