#Game 2048

from tkinter import *
from tkinter import messagebox
import random
import copy
global numArray
global cellArray
global newArray
global COLOR
global score
global scoreNum
score = 0
numArray = list()
cellArray = list()
newArray = list()
root = Tk()
root.title('2048')
root.geometry('320x380')
COLOR = ['gainsboro','antique white','lemon chiffon','alice blue',
         'cornflower blue','cyan','lime green','purple','DarkOliveGreen1',
         'SeaGreen1','thistle4','gold2']

def init():
    global numArray
    global cellArray
    global scoreNum
    for r in range(4):
        numArray.append([])
        cellArray.append([])
        for c in range(4):
            numArray[r].append(0)
            temp = Label(root,bg=COLOR[numArray[r][c]])
            temp.place(x=c*80, y=60+r*80, width=80, height=80)
            cellArray[r].append(temp)
    scoreLabel = Label(root,text=' \nSCORE:', font=5, justify=CENTER)
    scoreLabel.grid(row=0, column=0)
    scoreNum = Label(root,text='                        \n'+str(score), font=5, justify=RIGHT)
    scoreNum.grid(row=0,column=1,columnspan=10)
    grow(2)

def lose():
    messagebox.showinfo(title="Sorry.", message="You lose!")
    root.destroy()

def isfull():
    space = 0
    for r in range(4):
        for c in range(4):
            if newArray[r][c] == 0:
                space += 1
    if space == 0:
        return True
    else:
        return False

def ismovable():
    for r in range(4):
        for c in range(3):
            if newArray[r][c] == newArray[r][c+1]:
                return True
    for c in range(4):
        for r in range(3):
            if  newArray[r][c] == newArray[r+1][c]:
                return True
    return False

def check():
    if newArray != numArray:
        return True
    elif isfull() and ismovable():
        return False
    elif isfull() and not(ismovable()):
        lose()
        return None
    else:
        return False

def updateScore():
    global scoreLabel
    scoreNum.configure(text='                        \n'+str(score))

def grow(num):
    global newArray
    newArray = copy.deepcopy(numArray)
    place = list()
    for r in range(4):
        for c in range(4):
            if numArray[r][c] == 0:
                place.append((r,c))
    random.shuffle(place)
    for i in range(num):
        r,c = place[i]
        newArray[r][c] = random.sample([1,2],1)[0]
    redraw()

def redraw():
    global numArray
    global cellArray
    updateScore()
    for r in range(4):
        for c in range(4):
            if numArray[r][c] != newArray[r][c]:
                numArray[r][c] = newArray[r][c]
                num = newArray[r][c]
                if num == 0:
                    cellArray[r][c].configure(bg=COLOR[numArray[r][c]],text='')
                else:
                    cellArray[r][c].configure(bg=COLOR[numArray[r][c]],\
                                              text=str(2**num), \
                                              font=('Arial',35-len(str(2**num))*5))

def KeyUp(event):
    global newArray,score
    newArray = copy.deepcopy(numArray)
    for c in range(4):
        space = 0 # space to collide
        for r in range(4):
            if newArray[r][c] == 0:
                continue
            elif space == r:
                continue
            elif newArray[space][c] == 0:
                newArray[space][c] = newArray[r][c]
                newArray[r][c] = 0
            elif newArray[r][c] != newArray[space][c]:
                space += 1
                value = newArray[r][c]
                newArray[r][c] = 0
                newArray[space][c] = value
            else:
                newArray[space][c] += 1
                newArray[r][c] = 0
                score += 2**newArray[space][c]
                space += 1
    if check():
        redraw()
        grow(1)

def KeyDown(event):
    global newArray,score
    newArray = copy.deepcopy(numArray)
    for c in range(4):
        space = 3 # space to collide
        for r in range(3,-1,-1):
            if newArray[r][c] == 0:
                continue
            elif space == r:
                continue
            elif newArray[space][c] == 0:
                newArray[space][c] = newArray[r][c]
                newArray[r][c] = 0
            elif newArray[r][c] != newArray[space][c]:
                space -= 1
                value = newArray[r][c]
                newArray[r][c] = 0
                newArray[space][c] = value
            else:
                newArray[space][c] += 1
                newArray[r][c] = 0
                score += 2**newArray[space][c]
                space -= 1
    if check():
        redraw()
        grow(1)

def KeyLeft(event):
    global newArray,score
    newArray = copy.deepcopy(numArray)
    for r in range(4):
        space = 0 # space to collide
        for c in range(4):
            if newArray[r][c] == 0:
                continue
            elif space == c:
                continue
            elif newArray[r][space] == 0:
                newArray[r][space] = newArray[r][c]
                newArray[r][c] = 0
            elif newArray[r][c] != newArray[r][space]:
                space += 1
                value = newArray[r][c]
                newArray[r][c] = 0
                newArray[r][space] = value
            else:
                newArray[r][space] += 1
                newArray[r][c] = 0
                score += 2**newArray[r][space]
                space += 1
    if check():
        redraw()
        grow(1)

def KeyRight(event):
    global newArray,score
    newArray = copy.deepcopy(numArray)
    for r in range(4):
        space = 3 # space to collide
        for c in range(3,-1,-1):
            if newArray[r][c] == 0:
                continue
            elif space == c:
                continue
            elif newArray[r][space] == 0:
                newArray[r][space] = newArray[r][c]
                newArray[r][c] = 0
            elif newArray[r][c] != newArray[r][space]:
                space -= 1
                value = newArray[r][c]
                newArray[r][c] = 0
                newArray[r][space] = value
            else:
                newArray[r][space] += 1
                newArray[r][c] = 0
                score += 2**newArray[r][space]
                space -= 1
    if check():
        redraw()
        grow(1)

init()

root.bind("<KeyRelease-Up>", KeyUp)
root.bind("<KeyRelease-Down>", KeyDown)
root.bind("<KeyRelease-Left>", KeyLeft)
root.bind("<KeyRelease-Right>", KeyRight)

root.mainloop()
