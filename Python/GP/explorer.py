import pickle

#Use the following global variables to enable the pre-provided functions
'''Actually, you do not need to declare the global variables below here. You can either declare
them in the functions where it is assgined, or directly use these variables when assigning
them values in your main script.
The declaration is presented here only for better understanding of the coding.
'''

global maze #maze contains the maze information loaded from your original secret maze file,
            #identical to the maze information written to mazeFile.pkl, and changed when
            #the additional brick is added. It contains values:
            #0: empty block which is not explored
            #1: brick
            #2: START or the current position
            #3: GOAL
global currentPosition #This is the current position
global path #The previous path trajectory stored in explorerPath.pkl





#(1) File read: when keyboard event is activated, load maze
def LoadMaze():
    'Load the maze information into the global variable maze.'
    global maze
    file=open('mazeFile.pkl','rb')
    maze=pickle.load(file)
    file.close()


#(2) File read: load path and get current position
def ReadCurrentPosition():
    '''Get the previous stored path from explorerPath.pkl and put it to the global variable path.
Extract out the current position and put it in the global variable currentPosition.
Call this function when needed.'''
    global path, currentPosition
    file=open('explorerPath.pkl','rb')
    path=pickle.load(file)
    currentPosition=path[len(path)-1]
    file.close()

#(3) File read & write: load last path and store the new path
def WriteExplorerPath():
    file=open('explorerPath.pkl','rb')
    path=pickle.load(file)
    file.close()
    file=open('explorerPath.pkl','wb')
    path.append(currentPosition)
    pickle.dump(path,file)
    file.close()

#To Guest team: complete these functions. DO NOT change the function names. Otherwise, mazer.py can not call them.
    
def KeyUp(self):
    update()
    global currentPosition
    #To Guest team: complete this function. DO NOT change the function name, so that mazer.py can call it.
    ReadCurrentPosition()

    if maze[currentPosition[0]-1][currentPosition[1]]!=1:
        currentPosition=(currentPosition[0]-1,currentPosition[1])
        WriteExplorerPath()
        print('In Explorer: ',currentPosition)
    check()

def KeyDown(self):
    update()
    global currentPosition
    #To Guest team: complete this function. DO NOT change the function name, so that mazer.py can call it.
    ReadCurrentPosition()

    if maze[currentPosition[0]+1][currentPosition[1]]!=1:
        currentPosition=(currentPosition[0]+1,currentPosition[1])
        WriteExplorerPath()
        print('In Explorer: ',currentPosition)
    check()
        
def KeyLeft(self):
    update()
    global currentPosition
    #To Guest team: complete this function. DO NOT change the function name, so that mazer.py can call it.
    ReadCurrentPosition()

    if maze[currentPosition[0]][currentPosition[1]-1]!=1:
        currentPosition=(currentPosition[0],currentPosition[1]-1)
        WriteExplorerPath()
        print('In Explorer: ',currentPosition)
    check()
    
def KeyRight(self):
    update()
    global currentPosition
    #To Guest team: complete this function. DO NOT change the function name, so that mazer.py can call it.
    ReadCurrentPosition()

    if maze[currentPosition[0]][currentPosition[1]+1]!=1:
        currentPosition=(currentPosition[0],currentPosition[1]+1)
        WriteExplorerPath()
        print('In Explorer: ',currentPosition)
    check()
    
#To Guest team: write your coding in the part below.



def check():

    ReadCurrentPosition()
    check_one_way(START,END,0)
    if currentPosition == END:
        print('In Explorer: Congratulations! You have achieved the GOAL in %s steps!'%(len(path)-1))

def update():
    global START
    global END
    LoadMaze()
    for r in range(len(maze)):
        for c in range(len(maze)):
            if maze[r][c] == 2:
                START = (r,c)
            elif maze[r][c] == 3:
                END = (r,c)

def initialize():
    global choice
    global storage
    global largest_k
    choice = list()
    storage = list()
    largest_k = 0
    choice.append(False)

def isvalid(position):
    if (position in storage) or maze[position[0]][position[1]] == 1:
        return False
    else:
        return True

def find_way(position):

    num = 0
    for d in [(1,0),(-1,0),(0,1),(0,-1)]:

        newx = position[0]+d[0]
        newy = position[1]+d[1]
        temp = (newx,newy)
        
        if isvalid(temp):
            num+=1
            newposition = temp
        else:
            continue
    if num>0:
        return newposition,num
    return False
        

def check_one_way(position,end,k=0):
    global storage
    global choice
    global largest_k
    if position not in storage:
        storage.append(position)

    if position == end:
        initialize()

        return True
    
    if find_way(position):
        newposition,num = find_way(position)
        
        
        if num>1:
            k = k + 1
            if k > largest_k:
                choice.append(False)
                largest_k = k
            choice[k]=position
        return check_one_way(newposition,end,k)

    elif k>0:
        
        return check_one_way(choice[k],end,k-1)
    else:

        initialize()
        print('There is no way to go through the maze.')
        return False

initialize()
print('In Explorer: explorer.py initialized.')






    



