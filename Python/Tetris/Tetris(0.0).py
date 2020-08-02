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
    global stateArray, base, score, Score
    s = 0
    delete = []
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
            score += len(delete) * 10
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

    #print('freshing...')
def clear(block):
    global stateArray
    for vector in block.block:
        x = vector[0]
        y = vector[1]
        stateArray[x][y] = 0

def Rotate_Clock(root):
    global target, base
    newBlock = target.rotate(1)
    print(newBlock)
    if base == None:
        intersect = []
    else:
        intersect = list(set(newBlock)&set(base.block))
        
    if intersect != []:
        print("Invalid rotation")
    else:  
        clear(target)
        target.replace(newBlock)
        drawBlock(target)


def Rotate_CClock(root):
    global target
    newBlock = target.rotate(-1)
    #print(newBlock)
    clear(target)
    target.replace(newBlock)
    drawBlock(target)


def KeyLeft(root):
    global stateArray, target

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


            
def KeyDown(root):
    global stateArray, base, target, length

    newBlock = target.addVector((0,1))
    if base == None:
        clear(target)
        target.moveByVector((0, 1))
        drawBlock(target)
        if target.downBound + 1 == height:
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
            clear(target)
            target.moveByVector((0, 1))
            drawBlock(target)

        else:
            for i in range(len(target.block)):
                base.connect_block(target.block[i])
            target = generateBlock((random.randint(0,9),0),length)
            print("*********New block generated.**********")
            drawBlock(target)
    check()
            #print(base.block)
        

##    for y in range(height):
##        if sum(stateArray[x]) == width:
##            for x in range(width):
##                stateArray[height-1][c] = 0

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
    global pause
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
root.bind("<KeyPress-space>",Pause)
root.bind("<KeyPress-z>",Rotate_CClock)
root.bind("<KeyPress-x>",Rotate_Clock)
init()

'''    width = target.rightBound - target.leftBound
    height = target.upBound - target.downBound
    center = (target.leftBound+(width-1)/2,target.upBound+(height-1)/2)
    differx = center[0]
    differy = center[1]
    changex = 0
    newblock = list()
    for i in range(len(target.block)):
        tempx = target.block[i][0] - differx
        tempy = target.block[i][1] - differy
        newx = int(tempy + differx)-1
        newy = int(-tempx + differy)+3
        new = (newx,newy)
        newblock.append(new)
    newb = Block(newblock[0])
    print('target.block= ',target.block)
    print('step1.newblock = ',newb.block)
    for i in newblock:
        newb.connect_block(i)
    newb.getBound()
    print('step2.newblock = ',newb.block)
    print('newb.leftBound = ',newb.leftBound)
    print('newb.rightBound = ',newb.rightBound)
    if newb.leftBound < 0 :
        changey = - newb.leftBound
        newb.moveByVector((changex,0))
        print('Move right')
##    elif newb.rightBound >= width:
##        changex = width - 1 - newb.rightBound
##        newb.moveByVector((changex,0))
##        print('Move left')
    print('step3.newblock = ',newb.block)
    if base == None:
        clear(target)
        print('target.block before assign',target.block)
        target = copy.deepcopy(newb)
        print('target.block after assign',target.block)
        drawBlock(newb)
        print('step4.newblock = ',newb.block)
        print('=======================================')
        return None
    else:
        intersect = list(set(newb.block)&set(base.block))
        if intersect == [] :
            clear(target)
            target = newb
            drawBlock(newb)
        else:
            print('You can\'t rotate now.')
    
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
'''
