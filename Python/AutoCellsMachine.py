from tkinter import *
import copy,random

global height
global width
global cellArray
global colorArray
global newArray
global COLOR
global keepMoving
global step
height = 30
width = 30
cellArray = list()
colorArray = list()
newArray = list()

COLOR = ['white','black']
keepMoving = True
step = 0

root = Tk()
root.title('AutoCellsMachine')
root.geometry('%sx%s'%(width*20+60,height*20))

def start():
    global keepMoving
    keepMoving = True
    simulation()

def pause():
    global keepMoving
    keepMoving = False

def clear():
    global newArray
    global step
    pause()
    step = 0
    newArray = list()
    for r in range(height):
        newArray.append([])
        for c in range(width):
            newArray[r].append(0)
    stepLabel.configure(text='step'+'\n'+str(step))
    redraw()

def randomplace():
    global newArray
    clear()
    num = int(0.3*width*height)
    space=random.sample(range(width*height),num)
    space.sort()
    for cell in space:
        r = cell//height
        c = cell%height
        newArray[r][c] = 1
    redraw()

def click(i,j):
    global colorArray
    index = colorArray[i][j]
    colorArray[i][j] = 1 - index
    cellArray[i][j].configure(bg=COLOR[1-index])

def init():
    global cellArray
    for r in range(height):
        colorArray.append([])
        for c in range(width):
            colorArray[r].append(0)

    for r in range(height):
        cellArray.append([])
        newArray.append([])
        for c in range(width):
            newArray[r].append(0)
            exec('temp=Button(bg=COLOR[colorArray[%s][%s]],relief=\'flat\',\
    command=lambda:click(%s,%s))'%(r,c,r,c))
            exec('temp.place(width=20,height=20,x=20*c,y=20*r)')
            exec('cellArray[r].append(temp)')

def redraw():
    for r in range(height):
        for c in range(width):
            if colorArray[r][c] != newArray[r][c]:
                click(r,c)

def surrounding(i,j):
    count = 0
    for r in range (i-1,i+2):
        for c in range(j-1,j+2):
            if not(r == i and c == j) and colorArray[r][c] == 1:
                count+=1
    return count
    
       
def simulation():
    global newArray
    global step
    if keepMoving:
        newArray = copy.deepcopy(colorArray)
        for r in range(1,height-1):
            for c in range(1,width-1):

                if surrounding(r,c) == 3:
                    newArray[r][c] = 1
                elif surrounding(r,c) == 2:
                    continue
                else:
                    newArray[r][c] = 0

        step+=1
        stepLabel.configure(text='step'+'\n'+str(step))
        redraw()
        root.after(200,simulation)
    
startButton = Button(text='start',command=start)
startButton.place(x=width*20,y=0,height=40,width=60)
pauseButton = Button(text='pause',command=pause)
pauseButton.place(x=width*20,y=40,height=40,width=60)
clearButton = Button(text='clear',command=clear)
clearButton.place(x=width*20,y=80,height=40,width=60)
randomButton = Button(text='random',command=randomplace)
randomButton.place(x=width*20,y=120,height=40,width=60)
stepLabel = Label(text='step\n0')
stepLabel.place(x=width*20,y=height*20-40,height=40,width=60)
init()

root.mainloop()
        
