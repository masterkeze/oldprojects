from tkinter import *
from tkinter import ttk
from broken_line import *
import os

global closing_price

closing_price = broken_line()

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

titleChosen = ttk.Combobox(root,width = 5, state = 'readonly')
titleChosen['values'] = ('SH','SZ')
titleChosen.current(0)
titleChosen.place(x=width*49/64,y=10)

strategyChosen = ttk.Combobox(root,width = 16, state = 'readonly')
strategyChosen['values'] = ('均线突破策略')
#strategyChosen.current(0)
strategyChosen.place(x=width*49/64,y=45)


def go():
    global closing_price
    closing_price = broken_line()
    read_file(titleChosen.get()+'#'+entry_num.get())
    pass

def read_file(name):
    global closing_price
    os.chdir('M:\\Python\\wealth management')
    try:
        file = open(str(name)+'.txt','r')
        lines = file.readlines()
        file.close()
        print(lines[0],end='')
        for t in range(1,len(lines)-1):
            if lines[t][0].isdigit():
                temp = lines[t].split('\t')
                closing_price.add_point(name,temp[0],float(temp[4]))
        draw_line(closing_price)
                
    except:
        print("File not found.")

def draw_line(line):
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

    scatter = 0.03
    
    if type(line) == broken_line:
        high = line.highest
        low = line.lowest
        length = line.length
        C.create_line(gap,h-gap,gap,gap)#vertical line
        C.create_polygon(gap,gap,gap-5,gap+10,gap+5,gap+10)#vertical arrow
        value_step = ((1+scatter)*high-(1-scatter)*low)/v_split
        date_step = int(length/t_split + 0.99)
        for i in range(v_split+1):
            tempy = v_y_1 + i*v_step
            temp_value = round((1-scatter)*low + i*value_step,2)
            C.create_line(gap,tempy,w-gap,tempy,fill='gray')
            C.create_text(gap-15,tempy,text = temp_value)
            
        C.create_line(gap,h-gap,w-gap,h-gap)#horizonal line
        C.create_polygon(w-gap,h-gap,w-gap-10,h-gap-5,w-gap-10,h-gap+5)#horizonal arrow
        for i in range(t_split+1):
            tempx = v_x_1 + i*t_step
            temp_date = i*date_step+1
            C.create_line(tempx,h-gap,tempx,h-gap+5)
            C.create_text(tempx,h-gap+12,text=temp_date)
        
        C.create_text(gap,h-gap+30,text=line.points[0].date)#show start date
        C.create_text(w-gap,h-gap+30,text=line.points[length-1].date)#show end date
        last_x = None
        last_y = None
        for i in range(length):
            tempx = i*t_step/date_step + v_x_1
            tempy = (line.points[i].value - (1-scatter)*low)/value_step*v_step + v_y_1
            C.create_oval(tempx-2,tempy-2,tempx+2,tempy+2,fill = 'red',outline = 'red')
            if (last_x != None):
                C.create_line(last_x,last_y,tempx,tempy,fill = 'red')
            last_x = tempx
            last_y = tempy

goButton = Button(root,text = "GO",font = ('Arial',22),width = 7, command = go)
goButton.place(x=width*49/64,y=80)

##root.mainloop()
