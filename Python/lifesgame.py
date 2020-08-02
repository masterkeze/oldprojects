from tkinter import *
root = Tk()
root.title('life\'s game')
root.geometry('700x750+20+20')
row = 15
column = 15
initial_row = 7
initial_column = 7
initial_location = [initial_row,initial_column]
initial_direction = [0,-1]

previous_location = list()
previous_direction = list()

step = 0

class cell():
    def __init__(self,row,column):

        self.row = row
        self.column = column
        self.button = Button(root, text='', width = '5', height = '2', bg='white')
        self.color = 'white'
##        self.button.configure(command=Change(self.color))
        

    def show(self):
        self.button.grid(row=self.row,column=self.column)

    def __str__(self):
        return 'cell at %s row and %s column'%(self.row,self.column)

    def getcolor(self):
        return self.color
##def Change(color):
##    
##    try:
##        if color = 'white':
##            cell[][]
##        


def Press_next_step():
    global step
    global previous_location
    global previous_direction
    step = step+1
    current_location = list()
    if step == 1 :
        current_location = [initial_location[0],initial_location[1]]
        current_direction = [0,-1]
        ShowAnt(initial_location[0],initial_location[1])
    else:
        previous_row = previous_location[0]
        previous_column = previous_location[1]
        if cells[previous_row][previous_column].getcolor() == 'white':
            current_direction = TurnRight(previous_direction)
        else:
            current_direction = TurnLeft(previous_direction)
        current_location = [previous_location[0]+current_direction[0],previous_location[1]+current_direction[1]]
        ShowAnt(current_location[0],current_location[1])
        ChangeColor(cells[previous_row][previous_column])
    previous_location = [current_location[0],current_location[1]]
    previous_direction = [current_direction[0],current_direction[1]]
    step_label.configure(text='step = '+str(step))
    

def ChangeColor(cell):
    if cell.getcolor() == 'white':
        cell.button.configure(text='',bg='black')
        cell.color = 'black'
    else:
        cell.button.configure(text='',bg='white')
        cell.color = 'white'
    
        
def ShowAnt(row,column):
    ((cells[row][column]).button).configure(text='Ant',fg='red')

def TurnLeft(direction):
    new_direction = list()
    new_direction.append(direction[1])
    new_direction.append(-direction[0])
    return new_direction
    
def TurnRight(direction):
    new_direction = list()
    new_direction.append(-direction[1])
    new_direction.append(direction[0])
    return new_direction


cells = list()
for r in range(row):
    cells.append([])
    for c in range(column):
        temp = cell(r,c)
        cells[r].append(temp)
        temp.show()

##ShowAnt(initial_row,initial_column)

step_button = Button(root, text='Click to next step',width='20', height='2',command = Press_next_step)
step_button.grid(row = row+1, columnspan=4)

step_button = Button(root, text='Click to next 100 steps',width='20', height='2')
step_button.grid(row = row+1, column = 4, columnspan=4)

step_label = Label(root,text='step = '+str(step),height='2',font = '12')
step_label.grid(row = row+1, column = 12,columnspan = 3)

root.mainloop()
