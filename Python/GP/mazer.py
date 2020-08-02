from tkinter import *
import pickle
import explorer #Import explorer as a module and call its functions later.



# Use these global variables to enable the pre-provided functions.

'''Actually, you do not need to declare the global variables below here. You can either declare
them in the functions where it is assgined, or directly use these variables when assigning
them values in your main script.
The declaration is presented here only for better understanding of the coding.
'''
global currentPosition #This is the current position
global root #Define your Tk object as root
global maze #maze contains the maze information loaded from your original secret maze file,
            #identical to the maze information written to mazeFile.pkl, and changed when
            #the additional brick is added. It contains values:
            #0: empty block which is not explored
            #1: brick
            #2: START or the current position
            #3: GOAL
global tempMaze #tempMaze contains the maze information with explored blocks. It will not be 
                #written to mazeFile.pkl for read by explorer.py. Its difference with maze is
                #only in the new value below:
                #4: the block is previously empty and has been explored.
global labelCurrentPositionExplorer #It is the Label object showing the current position in
                                    #explore.py. CommunicationMazerExplorer() will update it
                                    #and thus we make it global variable
global START, GOAL
START=(6,1) #Position of START
GOAL=(1,6) #Position of GOAL



#(1) File write: only in initialization
#The functions below write the explorerPath.pkl for communication initialization with explorer.py.
#Just include it in the coding. You do not need to call it.

def InitializeExplorerPath():
    'Initialize explorerPath.pkl for explorer.py.   mazer.py write explorerPath.pkl only this time.'
    file=open('explorerPath.pkl','wb') #Overwrite the previous path information.
    pickle.dump([START], file)
    print('In Mazer: explorerPath.pkl initialized.')
    file.close()

InitializeExplorerPath() #Call InitializeExplorerPath()
                         #to initialize explorerPath.pkl at the begining of your file.

#The functions above write the explorerPath.pkl for communication initialization with explorer.py.
#Just include it in the coding. You do not need to call it.




#(2) File write: in initialization
#(3) File write: when a new brick is added
#The function below is pre-provided for writing mazeFile.pkl.
#Call it at appropriate place to coordinate mazer.py to explorer.py communication.

def WriteMazeFile():
    'Write the global variable maze to mazeFile.pkl for explorer.py to read.'
    file=open('mazeFile.pkl','wb')
    pickle.dump(maze, file)
    file.close()

#The function above is pre-provided for writing mazeFile.pkl.
#Call it at appropriate place to coordinate mazer.py to explorer.py communication.




#(4) File read: every 0.1s approximately
#The functions below are pre-provided for read from explorerPath.pkl around every 0.1 second and update
#the global variable tempMaze and the GUI.
# -- ReadCurrentPosition(): read from explorerPath.pkl, and assign current position to the global variable 
#    currentPosition. It is called in CommunicationMazerExplorer().
# -- CommunicationMazerExplorer(): read from explorerPath.pkl around every 0.1 second, and if there is move 
#    to a new position, update the the global variable tempMaze and show it in the GUI.
# -- UpdateTempMaze(previousPosition, currentPosition): update the global variable tempMaze and show it in
#    the GUI. !!! There is still need to write a function ReDraw to update the GUI.

def ReadCurrentPosition():
    '''Read the current position stored in currentPosition.pkl and assign to the global variable currentPosition.
After InitializeCommunicationFile(), only explorer.py can write currentPosition.pkl, and thus it is the latest current
position information after keyboard input. 
'''
    global currentPosition, path
    file=open('explorerPath.pkl','rb')
    path=pickle.load(file)
    currentPosition=path[len(path)-1]
    file.close()
        
def CommunicationMazerExplorer():# Use this function before the root.mainloop()
    ''' This function checks the new current position from Explorer, updates the labelCurrentPositionExplorer in GUI,
stores the new current position in path, and updates the global variable tempMaze (ReDraw the GUI in function UpdateMaze()).
CommunicationMazerExplorer() will be called around every 100 mini seconds.
'''
    global currentPosition, path
    previousPosition=currentPosition
    ReadCurrentPosition()#The global currentPosition will be changed by the position information in explorerPath.pkl    

    labelCurrentPositionExplorer.configure(text='In Explorer: \ncurrentPosition=(%s,%s)'%(currentPosition[0],currentPosition[1]),
                                           justify=CENTER)
    #labelCurrentPositionExplorer shows the current position feedback from Explorer.

    if currentPosition!=previousPosition:
        UpdateGUI(previousPosition,currentPosition)
        #This function only updates tempMaze, rather than maze, which is changed only when you add a brick.
        
    root.after(100, CommunicationMazerExplorer)#CommunicationMazerExplorer() will be called every 100 ms.

def UpdateGUI(previousPosition, currentPosition):
    '''Update the global varialble tempMaze, and then update GUI by ReDraw().
This function is called in CommunicationMazerExplorer().
You may not need to call it in your coding.'''
    global tempMaze
    tempMaze[previousPosition[0]][previousPosition[1]]=4
    tempMaze[currentPosition[0]][currentPosition[1]]=2
    ReDraw(previousPosition, currentPosition)    #For Host team: ReDraw will update the maze GUI. You need to write it. It does not need to return anything.







#The function below counts the number of bricks in the maze. Call it when needed.
    
def CountBricks():
    'It counts the brick number in the global variable maze, and return it.'
    brickNumber=0
    for mazeRow in maze:
        brickNumber+=mazeRow.count(1)# Add the number of 1s, i.e. bricks.
    return brickNumber


#The function above counts the number of bricks in the maze. Call it when needed.


#!!!Include the above code and use them in mazer.py. DO NOT modify them!!!


#Note to Host team:
#Write your coding below this line.

def ReDraw(previousPosition, currentPosition):
    'It will redraw the path on the GUI'
    newMaze[previousPosition[0]][previousPosition[1]].configure(text=str(len(path)-2),bg=COLOR[tempMaze[previousPosition[0]][previousPosition[1]]],image = '')
    newMaze[currentPosition[0]][currentPosition[1]].configure(bg=COLOR[tempMaze[currentPosition[0]][currentPosition[1]]],image = Image)
    labelCurrentPositionMazer.configure(text='In Mazer:\ncurrentPosition=(%s,%s)'%(currentPosition[0],currentPosition[1]))

file = open('SimpleTest.pkl','rb')
maze = pickle.load(file)
file.close()

WriteMazeFile()
print('In Mazer: mazeFile.pkl initialized.')

root = Tk()
root.geometry('480x520+700+200')
Image=PhotoImage(file='emoji.gif')
for r in range(len(maze)):
    for c in range(len(maze)):
        if maze[r][c] == 2:
            START = (r,c)
        elif maze[r][c] == 3:
            END = (r,c)
            
newMaze = list()
tempMaze = list()

COLOR=['white','black','yellow','blue','lightblue']

time = 0
def Click(i,j):
    global time
    color = COLOR[tempMaze[i][j]]
    if (color == 'white' or color == 'lightblue') and time == 0:
        newMaze[i][j].configure(bg='black')
        maze[i][j]=1
        time+=1
        labelBrickNumber.configure(text='Brick#:\n'+str(CountBricks()))
        WriteMazeFile()
        print('In Mazer: Event detected.')
        print('In Mazer: newMazeBlock = '+str((i,j))+'.')
        print('In Mazer: The new block is added!')
    elif time != 0:
        print('You can\'t add block any more!')
    else:
        print('You can\'t add block here!')

labelCurrentPositionMazer = Label(text='In Mazer:\ncurrentPosition=(10,1)')
labelCurrentPositionExplorer = Label(text='In Explorer:\ncurrentPosition=(10,1)')
BrickNumber = CountBricks()
labelBrickNumber = Label(text='Brick#:\n'+str(BrickNumber))

labelCurrentPositionMazer.place(x=0,y=0,width=160,height=40)
labelBrickNumber.place(x=200,y=0,width=80,height=40)
labelCurrentPositionExplorer.place(x=320,y=0,width=160,height=40)



for i in range(len(maze)):
    newMaze.append([])
    tempMaze.append([])
    for j in range(len(maze[0])):
        tempMaze[i].append(maze[i][j])
        exec('newMaze[%s].append(Button(root,bg=COLOR[maze[%s][%s]],fg=\'gray\',\
relief=\'flat\',command=lambda:Click(%s,%s)))'%(i,i,j,i,j))
        newMaze[i][j].place(x=40*j,y=40*i+40,width=40,height=40)
        if START == (i,j):
            newMaze[i][j].configure(image = Image)


ReadCurrentPosition()






#Note To Host team:
#Write your coding above this line.



#!!!Include the coding below as the end of the mazer.py. DO NOT modify them!!!
        
root.bind("<KeyRelease-Up>", explorer.KeyUp)
root.bind("<KeyRelease-Down>", explorer.KeyDown)
root.bind("<KeyRelease-Left>", explorer.KeyLeft)
root.bind("<KeyRelease-Right>", explorer.KeyRight)
CommunicationMazerExplorer()

root.mainloop()
