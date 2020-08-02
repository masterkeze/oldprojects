#Tetris

from tkinter import *
import random,copy,random

global height, width, cellArray, colorArray, oldArray, colorbase, reliefbase
global base, focus, score, pause, length


start = (0,0)
height = 16
width = 10
length = 4

colorbase = ['white','cyan']
reliefbase = ['flat','raised']




def is_linked(vector1,vector2):
    difference = (vector1[0]-vector2[0],vector1[1]-vector2[1])
    choice = [(0,1),(0,-1),(1,0),(-1,0)]
    if difference in choice:
        return True
    else:
        return False

class Block():
    def __init__(self,initial):
        self.block = [initial]
        self.head = self.block[0]
        self.tail = self.block[len(self.block)-1]
        self.leftBound = initial[0]
        self.rightBound = initial[0]
        self.upBound = initial[1]
        self.downBound = initial[1]
        self.length = len(self.block)
        self.lowest = initial
        
    def add_block(self,vector):
        x = vector[0]
        y = vector[1]
        if is_linked(vector,self.tail) and not(vector in self.block):
            if y > self.downBound:
                self.lowest = vector
            self.block.append(vector)
            self.leftBound = min(self.leftBound,x)
            self.rightBound = max(self.rightBound,x)
            self.upBound = min(self.upBound,y)
            self.downBound = max(self.downBound,y)
            self.tail = vector
            self.length += 1
        else:
            pass
            #print('New block is unconnected to the old block.')
    def connect_block(self,vector):
        if vector not in self.block:
            self.block.append(vector)
            self.length + 1
            
    def delete_block(self,vector):
        if vector in self.block:
            del(self.block[self.block.index(vector)])
            self.length - 1

    def moveByVector(self,vector):
        newBlock = list()
        x = vector[0]
        y = vector[1]
        
        for i in range(self.length):
            temp = (self.block[i][0]+x,self.block[i][1]+y)
            newBlock.append(temp)
            
        self.block = newBlock
        self.leftBound += x
        self.rightBound += x
        self.upBound += y
        self.downBound += y
        self.lowest = (self.lowest[0]+x,self.lowest[1]+y)

    def addVector(self,vector):
        newBlock = list()
        x = vector[0]
        y = vector[1]
        
        for i in range(self.length):
            temp = (self.block[i][0]+x,self.block[i][1]+y)
            newBlock.append(temp)
            
        return newBlock

    def getBound(self):
        self.leftBound = None
        for i in self.block:
            x = i[0]
            y = i[1]
            if self.leftBound == None:
                self.leftBound = x
                self.rightBound = x
                self.upBound = y
                self.downBound = y
                self.lowest = i
            else:
                self.leftBound = min(self.leftBound,x)
                self.rightBound = max(self.rightBound,x)
                self.upBound = min(self.upBound,y)
                self.downBound = max(self.downBound,y)
                if y == self.downBound:
                    self.lowest = i
    
    def rotate(self,sign):
        'sign= 1:clockwise'
        'sign=-1:counter-clockwise'
        mid = (self.leftBound + self.rightBound)/2
        temp_block = list()
        temp_upBound = None
        for instance in self.block:
            temp_x = instance[0]
            temp_y = instance[1]
            new_x = sign*temp_y
            new_y = -1*sign*temp_x
            temp_block.append((new_x,new_y))
            if temp_upBound == None:
                temp_upBound = new_y
                temp_leftBound = new_x
                temp_rightBound = new_x
            else:
                temp_upBound = min(temp_upBound,new_y)
                temp_leftBound = min(temp_leftBound,new_x)
                temp_rightBound = max(temp_rightBound,new_x)
        temp_mid = (temp_leftBound + temp_rightBound)/2
        dif_y = int(self.upBound - temp_upBound)
        dif_x = int(mid - temp_mid)
        newBlock = list()
        for i in temp_block:
            temp_x = i[0]
            temp_y = i[1]
            new_x = temp_x + dif_x
            new_y = temp_y + dif_y
            newBlock.append((new_x,new_y))
        return newBlock

    def replace(self,newBlock):
        for i in self.block:
            self.delete_block(i)
        self.block = newBlock
        self.getBound()
        print('New block replaced.')
            
        
        
def generateBlock(initial,length):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    b = Block(initial)
    while b.length < length:
        vector = random.sample(direction,1)[0]
        newBlock = (b.tail[0]+vector[0], b.tail[1]+vector[1])
        if newBlock[0] >= 0 and newBlock[1] >= 0 and newBlock[0] < width-1:
            b.add_block(newBlock)
    print(b.block)
    return b


def init():
    global oldArray, target, score, cellArray, stateArray, focus, base, pause, Score, length
    score = 0
    cellArray = list()
    stateArray = list()
    oldArray = list()
    pause = False
    base = None
    focus = None
    
    main = Label(root,bg='gray',relief='flat')
    main.place(width=480,height=500,x=start[0],y=start[1])
    ScoreText = Label(root,text='Score:',bg='gray',fg='yellow',relief='flat',font=(font,20),justify=LEFT)
    ScoreText.place(x=start[0]+width*30+10,y=start[1]+430)
    Score = Label(root,text=str(score),bg='gray',fg='yellow',relief='flat',font=(font,18),justify=LEFT)
    Score.place(x=start[0]+width*30+10,y=start[1]+460)
    for x in range(width):
        cellArray.append([])
        stateArray.append([])
        for y in range(height):
            temp = Label(root,bg='white',relief='flat')
            temp.place(width=30,height=30,\
                       x=30*x+start[0]+10,y=30*y+start[1]+10)
            cellArray[x].append(temp)
            stateArray[x].append(0)
    oldArray = copy.deepcopy(stateArray)

    target = generateBlock((random.randint(0,9),0),length)
    drawBlock(target)
    frame()
    moveDown()

def check():
    global stateArray, base, score, Score, target
    s = 0
    delete = []
    newBlock = target.addVector((0,1))
    if base == None:
        if target.downBound + 1 == height:
            score += 10
            Score.configure(text=str(score))
            base = Block(target.lowest)
            for i in range(len(target.block)):
                base.connect_block(target.block[i])
            target = generateBlock((random.randint(0,9),0),length)
            print("*********New block generated.**********")
            drawBlock(target)
            #print(base.block)
    else:
        intersect = list(set(newBlock)&set(base.block))
        if intersect == [] and target.downBound + 1 != height:
            pass

        else:
            score += 10
            Score.configure(text=str(score))
            for i in range(len(target.block)):
                base.connect_block(target.block[i])
            target = generateBlock((random.randint(0,9),0),length)
            print("*********New block generated.**********")
            drawBlock(target)
            
    for b in target.block:
        i = b[0]
        j = b[1]
        if base != None and (i,j) in base.block:
            print ('gameOver')
            GameOver()
            Pause(root)
            return 0
        
    if base != None:
        for y in range(height-1,-1,-1):
            s = 0
            for x in range(width):
                if (x,y) in base.block and stateArray[x][y] == 1:
                    s += 1
                    
            if s == width:
                delete.append(y)

        if delete != []:
            print(delete)
            delete.sort()
            score += len(delete) * 100
            Score.configure(text=str(score))
            print(delete)
            clear(base)
            update()
            for d in delete:
                for x in range(width):
                    base.delete_block((x,d))
                    stateArray[x][d] = 0
                    update()

            for d in delete:
                for y in range(d-1,-1,-1):
                    for x in range(width):
                        if (x,y) in base.block:
                            base.delete_block((x,y))
                            base.connect_block((x,y+1))

            drawBlock(base)

def frame():
    global stateArray,oldArray
    if pause == True:
        return 0
    update()

    oldArray = copy.deepcopy(stateArray)
    root.after(100,frame)

def drawBlock(block):
    for i in block.block:
        stateArray[i[0]][i[1]] = 1

def update():
    global cellArray
    for y in range(height):
        for x in range(width):
##            if stateArray[x][y] != oldArray[x][y]:
                index = stateArray[x][y]
                cellArray[x][y].configure(bg=colorbase[index],\
                                          relief=reliefbase[index])

def clear(block):
    global stateArray
    for vector in block.block:
        x = vector[0]
        y = vector[1]
        stateArray[x][y] = 0

def Rotate_Clock(root):
    global target, base
    if pause == True:
        return 0
    newBlock = target.rotate(1)
    #print(newBlock)
    newBlock.sort()
    leftBound = newBlock[0][0]
    rightBound = newBlock[len(newBlock)-1][0]
    modify = 0
    if leftBound < 0:
        modify = -1 * leftBound
    elif rightBound > width - 1:
        modify = width - 1 - rightBound
    update_block = list()
    for i in newBlock:
        update_block.append((i[0]+modify,i[1]))
    if base == None:
        intersect = []
    else:
        intersect = list(set(update_block)&set(base.block))
        
    if intersect != []:
        print("Invalid rotation")
    else:  
        clear(target)
        target.replace(update_block)
        drawBlock(target)
    check()


def Rotate_CClock(root):
    global target
    if pause == True:
        return 0
    newBlock = target.rotate(-1)
    #print(newBlock)
    newBlock.sort()
    leftBound = newBlock[0][0]
    rightBound = newBlock[len(newBlock)-1][0]
    modify = 0
    if leftBound < 0:
        modify = -1 * leftBound
    elif rightBound > width - 1:
        modify = width - 1 - rightBound
    update_block = list()
    for i in newBlock:
        update_block.append((i[0]+modify,i[1]))
    if base == None:
        intersect = []
    else:
        intersect = list(set(update_block)&set(base.block))
        
    if intersect != []:
        print("Invalid rotation")
    else:  
        clear(target)
        target.replace(update_block)
        drawBlock(target)
    check()


def KeyLeft(root):
    global stateArray, target
    if pause == True:
        return 0
    newBlock = target.addVector((-1,0))
    if target.leftBound != 0:
        if base == None:
            clear (target)
            target.moveByVector((-1,0))
            drawBlock(target)
        else:
            intersect = list(set(newBlock)&set(base.block))
            if intersect == [] :
                clear(target)
                target.moveByVector((-1, 0))
                drawBlock(target)

def KeyRight(root):
    global stateArray, target
    if pause == True:
        return 0
    newBlock = target.addVector((1,0))
    if target.rightBound != width - 1:
        if base == None:
            clear (target)
            target.moveByVector((1,0))
            drawBlock(target)
        else:
            intersect = list(set(newBlock)&set(base.block))
            if intersect == [] :
                clear(target)
                target.moveByVector((1, 0))
                drawBlock(target)

def KeyFall(root):
    global target, base, width, height
    if pause == True:
        return 0
    modify = 0
    newBlock = []
    boundary = []
    intersect = []
    while intersect == []:
        modify += 1
        for i in target.block:
            newBlock.append((i[0],i[1] + modify))
        for i in range(width):
            boundary.append((i,height))
        if base == None:
            intersect = list(set(newBlock)&set(boundary))
        else:
            intersect = list(set(newBlock)&(set(base.block)|set(boundary)))
    clear(target)
    target.moveByVector((0, modify-1))
    drawBlock(target)
    check()
            
def KeyDown(root):
    global stateArray, base, target, height
    if pause == True:
        return 0
    newBlock = target.addVector((0,1))
    if base == None:
        clear(target)
        target.moveByVector((0, 1))
        drawBlock(target)

    else:
        intersect = list(set(newBlock)&set(base.block))
        if intersect == [] and target.downBound + 1 != height:
            clear(target)
            target.moveByVector((0, 1))
            drawBlock(target)


    check()
    
def Pause(root):
    global pause
    print(pause)
    if pause == False:
        pause = True
        return 0
    else:
        pause = False
        moveDown()
        print("continue")
        return 0
    
def Restart():
    global pause, gameover
    gameover.destroy()

    init()
    
def GameOver():
    global gameover
    gameover = Tk()
    gameover.title('Game Over!')
    gameover.geometry('300x300+390+80')
    lgameover = Label(gameover,text='Game Over!',font=(font,20),justify = CENTER)
    lgameover.place(x=20,y=30,width=260, height=100)
    bgameover = Button(gameover,text='Restart',font=(font,35),\
                       justify = CENTER,command=Restart)
    bgameover.place(x=20,y=160,width=260, height=100)
    
def moveDown():
    global pause
    #print(pause)
    if pause == True:
        return 0
    KeyDown(root)
    root.after(1000,moveDown)


root = Tk()
root.title('Tetris')
root.geometry('480x500+300+50')
root.bind("<KeyPress-Left>",KeyLeft)
root.bind("<KeyPress-Right>",KeyRight)
root.bind("<KeyPress-Down>",KeyDown)
root.bind("<KeyRelease-space>",KeyFall)
root.bind("<KeyRelease-z>",Rotate_CClock)
root.bind("<KeyRelease-x>",Rotate_Clock)
init()
