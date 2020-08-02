from tkinter import *
import copy,random
global length
#rule B2/S34
COLOR = ["SteelBlue1","gold2"]
length = 25
gap = 5
size = 8
quadrant_a = list()
quadrant_b = list()
quadrant_c = list()

for i in range(size):
    quadrant_a.append([])
    quadrant_b.append([])
    quadrant_c.append([])
    for j in range(size):
        quadrant_a[i].append(1)
        quadrant_b[i].append(1)
        quadrant_c[i].append(1)

def get_value(x,y,z):
    if x*y*z == 0:
        if z == 0:
            return quadrant_a[x][y]
        elif x == 0:
            return quadrant_b[y][z]
        else:
            return quadrant_c[z][x]
    else:
        print("Invalid input")

def change_value(x,y,z,value):
    if x*y*z == 0:
        if z == 0:
            quadrant_a[x][y] = value
        elif x == 0:
            quadrant_b[y][z] = value
        else:
            quadrant_c[z][x] = value
    else:
        print("Invalid input")

def get_coord(x,y,z):
    basex,basey = get_center(x,y,z)
    x1 = basex - 0.5*length
    y1 = basey - 3**0.5/2*length
    x2 = x1 + length
    y2 = y1
    x3 = basex + length
    y3 = basey
    x4 = x2
    y4 = basey + 3**0.5/2*length
    x5 = x4 - length
    y5 = y4
    x6 = basex - length
    y6 = basey
    return x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6

def get_center(x,y,z):
    basex = (x*_x[0]+y*_y[0]+z*_z[0])*(2*length+gap-size)+center[0]
    basey = (x*_x[1]+y*_y[1]+z*_z[1])*(2*length+gap-size)+center[1]
    return basex,basey


root = Tk()
root.geometry('800x800+100+50')
root.title("HexCellMachine")
C = Canvas(root, bg ='white', height=800, width=800)
C.place(x=0,y=0)

center = (400,400)
_x = (3**0.5/2,1/2)
_y = (0,-1)
_z = (-3**0.5/2,1/2)
def draw():
    for i in range(size):
        for j in range(size):
            x,y,z = j,i,0
            for t in range(3):
                coord = get_coord(x,y,z)
                color = COLOR[get_value(x,y,z)]
                exec("HexCell_%s_%s_%s = C.create_polygon(coord,fill=color)"%(x,y,z))
                x,y,z = y,z,x
    C.update()
draw()
def main():
    change_value(6,6,0,0)
    draw()
'''
x = 100
y = 230
for i in range(2*size-1):
    if i < size:
        basex = x
        basey = y + i*3**0.5*(length+gap)
        for j in range(size+i):
            C.create_polygon(get_coord(basex,basey),fill="gold2",tag="%s%s"%(i,j) )
            temp = basex
            basex += 1.5*(length+gap)
            basey -= 3**0.5/2*(length+gap)
    else:
        basex = temp
        basey = y + (i-size+1)*3**0.5*(length+gap)
        for j in range(3*size-i-2):
            C.create_polygon(get_coord(basex,basey),fill="gold2")
            basex -= 1.5*(length+gap)
            basey += 3**0.5/2*(length+gap)
'''


