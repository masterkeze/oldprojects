from tkinter import *
from tkinter import ttk
from broken_line import *
from strategy import *
import os
import math
global closing_price, drawing_line

closing_price = broken_line()
drawing_line = None

####################################################################
global show_limit

show_limit = 1000

####################################################################
width = 800
height = 600
root = Tk()
root.title("Strategy Test")
root.geometry('%sx%s+100+50'%(width,height))

C = Canvas(root, bg='alice blue',height = height*3/4, width = width*3/4)
C.place(x=0,y=0)

code_num = StringVar()
entry_num = Entry(root,textvariable = code_num, width = int(width/64), borderwidth = 2)
code_num.set('600000')
entry_num.place(x=width*56/64,y=10)

titleChosen = ttk.Combobox(root,width = 7*int(width/400-0.5), state = 'readonly')
titleChosen['values'] = ('SH','SZ')
titleChosen.current(0)
titleChosen.place(x=width*49/64,y=10)

strategyChosen = ttk.Combobox(root,width = 22*int(width/400-0.5), state = 'readonly')
strategyChosen['values'] =('market_trend','profit_trend')
strategyChosen.current(0)
strategyChosen.place(x=width*49/64,y=45)



def go():
    global closing_price, drawing_line
    closing_price = broken_line()
    
    closing_price = read_file(titleChosen.get()+'#'+entry_num.get())
    if closing_price == None:
        return None
    if strategyChosen.get() == 'market_trend':
        drawing_line = closing_price

    if strategyChosen.get() == 'profit_trend':
        s = strategy()
        s.short_period = 7
        s.long_period = 15
        for t in range(closing_price.length):
            s.update(closing_price.points[t])
        drawing_line = s.get_line()
        #drawing_line = s.holding_line

    set_scale(drawing_line.length)
    set_limit_scale(drawing_line.length)
    redraw(0)
    analyze(drawing_line)

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
        
    status_label["text"]="总收益:\n"+str(round(total_rate,2))+"%\n"+\
                          "平均年收益:\n"+str(round(annual_rate,2))+"%\n"+\
                          "最大回撤:\n"+str(round(temp_drop,2))+"%\n"+\
                          "夏普率:\n"+str(round(total_rate/temp_drop,2))

def read_file(name):
    global closing_price,drawing_line
    os.chdir('M:\\Python\\wealth management')
    try:
        file = open(str(name)+'.txt','r')
        lines = file.readlines()
        file.close()
        print(lines[0],end='')
        temp_line = broken_line()
        for t in range(1,len(lines)-1):
            if lines[t][0].isdigit():
                temp = lines[t].split('\t')
                temp_line.add_point(name,temp[0],float(temp[4]))

        return temp_line
            
    except:
        print("File not found.")
        return None

def redraw(x):
    global drawing_line
    if drawing_line != None:
        draw_line(drawing_line,x)

def set_scale(length):
    scale["from_"] = 0
    scale["to"] = length - show_limit
    scale["resolution"] = int(0.05*show_limit)
    scale["command"] = redraw

def set_limit(x):
    global show_limit
    show_limit = int(x)
    if drawing_line != None:
        set_scale(drawing_line.length)
        redraw(0)

def set_limit_scale(length):

    limit_scale["to"] = length
    limit_scale["resolution"] = 10

def draw_line(line,x):
    x=int(x)
    scatter = 0
    
    if type(line) == broken_line:

        C.delete(ALL)

        h = 3/4*height
        w = 3/4*width
        gap = 1/15*width
        
        t_split = 10
        t_x_1 = gap
        t_y_1 = h-gap
        t_x_2 = w-gap-15
        t_y_2 = h-gap
        t_step = (t_x_2-t_x_1)/t_split
        
        v_split = 5
        v_x_1 = gap
        v_y_1 = h-gap-15
        v_x_2 = gap
        v_y_2 = gap + 15
        v_step = (v_y_2-v_y_1)/v_split

        high = line.highest
        low = line.lowest
        length = line.length

        C.create_line(gap,h-gap,gap,gap)#vertical line
        C.create_polygon(gap,gap,gap-5,gap+10,gap+5,gap+10)#vertical arrow
        value_step = ((1+scatter)*high-(1-scatter)*low)/v_split
        date_step = int(min(length-x,show_limit)/t_split + 0.99)
        for i in range(v_split+1):
            tempy = v_y_1 + i*v_step
            temp_value = round((1-scatter)*low + i*value_step,2)
            C.create_line(gap,tempy,w-gap,tempy,fill='gray')
            C.create_text(gap-20,tempy,text = temp_value)
            
        C.create_line(gap,h-gap,w-gap,h-gap)#horizonal line
        C.create_polygon(w-gap,h-gap,w-gap-10,h-gap-5,w-gap-10,h-gap+5)#horizonal arrow
        for i in range(t_split+1):
            tempx = v_x_1 + i*t_step
            temp_date = x+i*date_step
            C.create_line(tempx,h-gap,tempx,h-gap+5)
            C.create_text(tempx,h-gap+12,text=temp_date)
        
        C.create_text(gap,h-gap+30,text=line.points[0].date)#show start date
        C.create_text(w-gap,h-gap+30,text=line.points[length-1].date)#show end date
        last_x = None
        last_y = None
        x=int(x)
        for i in range(x,min(x-1+show_limit,length)):
            tempx = (i-x+1)*t_step/date_step + v_x_1
            tempy = (line.points[i].value - (1-scatter)*low)/value_step*v_step + v_y_1
##            if (line.points[i].value == high):
##                C.create_line(tempx-3,tempy-5,tempx-7,tempy-15,fill = 'black')
##                C.create_text(tempx-7,tempy-20,text = high)
            #C.create_oval(tempx-2,tempy-2,tempx+2,tempy+2,fill = 'red',outline = 'red')
            if (last_x != None and last_y != None):
                C.create_line(last_x,last_y,tempx,tempy,fill = 'red')
            last_x = tempx
            last_y = tempy

goButton = Button(root,text = "GO",font = ('Arial',22),width = 7, command = go)
goButton.place(x=width*49/64,y=80)

scale = Scale(root,orient = HORIZONTAL,showvalue=0)
scale.place(x=0,y=3/4*height,width=3/4*width)

limit_scale = Scale(root,orient = HORIZONTAL,from_=10, command = set_limit,label = 'Show Limit')
limit_scale.place(x=30,y=3/4*height+30)

status_label = Label(root,text = "status aera",anchor="nw",justify=LEFT,font=(font,20),relief = GROOVE)
status_label.place(x = width*49/64,y=150,width = (1/4 - 1/32)*width,height = 1/2*height)

root.mainloop()
