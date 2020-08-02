from tkinter import *
import copy,random
global tempArray
h = w = 4

size = 60 - 3*(h//2)# Control the size of each cell.
height = h + 2
width = w + 2
cellArray = list()
colorArray = list()
tempArray = list()
newArray = list()
hint = '●'
COLOR = ['gray','black','blue']
root = Tk()
root.title('Light the light.')
root.geometry('%sx%s+10+10'%(width*size+60,height*size))

def change(i,j):
    global tempArray
    tempArray[i-1][j] = 2 - tempArray[i-1][j]
    tempArray[i][j] = 2 - tempArray[i][j]
    tempArray[i+1][j] = 2 - tempArray[i+1][j]
    tempArray[i][j-1] = 2 - tempArray[i][j-1]
    tempArray[i][j+1] = 2 - tempArray[i][j+1]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def getstep(num):
    if num == 0:
        return 1
    else:
        s = int(factorial(w)/(factorial(num)*factorial(w-num)))
        return s + getstep(num-1)

def solution():
    global tempArray
    global storage
    keepgoing = True
    storage = list()
    num = 0
    while keepgoing:
        answer = list()
        choice_range = list(range(1,w+1))
        choice = list()
        while True:
            choice = random.sample(choice_range,num)
            choice.sort()
            if choice not in storage:
                storage.append(choice)
                break            
        tempArray = copy.deepcopy(colorArray)
        keepgoing = False
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 and c in choice:
                    change(r,c)
                    answer.append((r,c))
                elif r > 1 and tempArray[r-1][c] == 0:
                    change(r,c)
                    answer.append((r,c))
        for c in range(1,w+1):
            if tempArray[h][c] == 0:
                keepgoing = True
                break
        if not(keepgoing):
            break
        if len(storage) == getstep(num):
            num += 1
    return answer

def click(i,j):
    global colorArray
    index = colorArray[i][j]
    if cellArray[i][j]['text'] == hint:
        cellArray[i][j].configure(text='')
    if index ==0 or index == 2:
        colorArray[i-1][j] = 2 - colorArray[i-1][j]
        cellArray[i-1][j].configure(bg=COLOR[colorArray[i-1][j]])
        colorArray[i][j] = 2 - colorArray[i][j]
        cellArray[i][j].configure(bg=COLOR[colorArray[i][j]])
        colorArray[i+1][j] = 2 - colorArray[i+1][j]
        cellArray[i+1][j].configure(bg=COLOR[colorArray[i+1][j]])
        colorArray[i][j-1] = 2 - colorArray[i][j-1]
        cellArray[i][j-1].configure(bg=COLOR[colorArray[i][j-1]])
        colorArray[i][j+1] = 2 - colorArray[i][j+1]
        cellArray[i][j+1].configure(bg=COLOR[colorArray[i][j+1]])

def init():
    global cellArray
    for r in range(height):
        colorArray.append([])
        for c in range(width):
            if r == 0 or r == height-1 or c == 0 or c == width-1:
                colorArray[r].append(1)
            else:
                colorArray[r].append(0)

    for r in range(height):
        cellArray.append([])
        newArray.append([])
        for c in range(width):
            newArray[r].append(0)
            exec('temp=Button(bg=COLOR[colorArray[%s][%s]],\
    command=lambda:click(%s,%s))'%(r,c,r,c))
            exec('temp.place(width=size,height=size,x=size*c,y=size*r)')
            exec('cellArray[r].append(temp)')
            
def clear():
    global colorArray
    for r in range(1,height-1):
        for c in range(1,height-1):
            colorArray[r][c] = 0
            cellArray[r][c].configure(bg=COLOR[0])
            
def showAnswer():
    answer = solution()
    for r in range(1,h+1):
        for c in range(1,w+1):
            cellArray[r][c].configure(text='')
            if (r,c) in answer :
                cellArray[r][c].configure(text=hint,fg = 'yellow')
    

clearButton = Button(root,text='clear',command=clear)
clearButton.place(x=width*size,y=0,height=40,width=60)
solutionButton = Button(root,text='show',command=showAnswer)
solutionButton.place(x=width*size,y=40,height=40,width=60)
init()
root.mainloop()
