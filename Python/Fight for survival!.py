class gene():
    def __init__(self,string='00000'):
        self.gene = string

class creature():
    def __init__(self,gene = None):
        self.gene = gene
        self.level = 1

    def isliving(self):
        if level == 10:
            return False

from tkinter import *
import random,time

height = 400
width = 600
diameter = 5

def draw_creature(x,y,diameter,tag):
    radius = diameter/2
    coord = x-radius,y-radius,x+radius,y+radius
    C.create_oval(coord,fill='green',tag=tag,outline='green')
    C.update()

root = Tk()
root.title('Fight for survival!')
root.geometry('%sx%s+100+100'%(width,height))
C = Canvas(root, bg='gray', height=height,width=width)
C.place(x=-2,y=-2)

for t in range(1000):
    xcoord = 600*random.random()
    ycoord = 400*random.random()
    draw_creature(xcoord,ycoord,diameter,'green'+str(t))
    time.sleep(0.03)

root.mainloop()
