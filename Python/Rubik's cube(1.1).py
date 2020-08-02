# Rubik's cube
import copy
from tkinter import *
global i,j,k,_i,_j,_k,position,oriention,cubeArray
global Tx1,Tx2,Tx3,_Tx1,_Tx2,_Tx3
global Ty1,Ty2,Ty3,_Ty1,_Ty2,_Ty3
global Tz1,Tz2,Tz3,_Tz1,_Tz2,_Tz3


class vector():
    def __init__(self,name,x,y,z):
        self.name = str(name)
        if self.name.find('__') != -1:
            self.name = self.name.replace('__','')
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return self.name

    def reverse(self):
        self.name = '_'+self.name
        if self.name.find('__') != -1:
            self.name = self.name.replace('__','')
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z

class cube:
    def __init__(self,location,color,direction):
        
        self.location = location
        self.color = color
        self.direction = direction

    def __repr__(self):
        return str(self.color)+','+str(self.direction)


def matrix_product_p(a,b):
    'This one is professional.'
    output = list()
    if len(a[0]) != len(b):
        print('Invalid product.')
        return None
    if type(b[0][0]) != vector :
        for r in range(len(a)):
            output.append([])
            for c in range(len(b[0])):
                s = 0
                for temp in range(len(a[0])):
                    s += a[r][temp] * b[temp][c]
                output[r].append(s)
        return output
    else:
        for r in range(len(a)):
            output.append([])
            for c in range(len(b[0])):
                s = 0
                for temp in range(len(a[0])):
                    if a[r][temp] == 0:
                        continue
                    elif a[r][temp] == 1:
                        s = b[temp][c]
                    elif a[r][temp] == -1:
                        s = vector('_'+b[temp][c].name,-b[temp][c].x,-b[temp][c].y,-b[temp][c].z)

                output[r].append(s)
        return output

def matrix_product(a,b):
    'This one is specified. Just for this file.'
    output = list()
    if len(a[0]) != len(b):
        print('Invalid product.')
        return None
    if type(b[0]) != vector :
        for r in range(len(a)):
            s = 0
            for temp in range(len(a[0])):
                s += a[r][temp] * b[temp]
            output.append(s)
        return output
    
    else:
        for r in range(len(a)):
            s = 0
            for temp in range(len(a[0])):
                if a[r][temp] == 0:
                    continue
                elif a[r][temp] == 1:
                    s = b[temp]
                elif a[r][temp] == -1:
                    s = vector('_'+b[temp].name,-b[temp].x,-b[temp].y,-b[temp].z)
            output.append(s)
        return output

def initialize():
    global i,j,k,_i,_j,_k,position,oriention,cubeArray
    global Tx1,Tx2,Tx3,_Tx1,_Tx2,_Tx3
    global Ty1,Ty2,Ty3,_Ty1,_Ty2,_Ty3
    global Tz1,Tz2,Tz3,_Tz1,_Tz2,_Tz3
    global x,y,z
    
    i = vector('i',1,0,0)
    j = vector('j',0,1,0)
    k = vector('k',0,0,1)
    _i = vector('_i',-1,0,0)
    _j = vector('_j',0,-1,0)
    _k = vector('_k',0,0,-1)

    Tx1 = [[1,0,0],
           [0,0,1],
           [0,-1,0]]#色位
    Tx2 = matrix_product_p(Tx1,Tx1)
    Tx3 = matrix_product_p(Tx2,Tx1)
    _Tx1 = copy.deepcopy(Tx3)#块位
    _Tx2 = copy.deepcopy(Tx2)
    _Tx3 = copy.deepcopy(Tx1)

    
    Ty1 = [[0,0,-1],
           [0,1,0],
           [1,0,0]]
    Ty2 = matrix_product_p(Ty1,Ty1)
    Ty3 = matrix_product_p(Ty2,Ty1)
    _Ty1 = copy.deepcopy(Ty3)
    _Ty2 = copy.deepcopy(Ty2)
    _Ty3 = copy.deepcopy(Ty1)


    Tz1 = [[0,1,0],
           [-1,0,0],
           [0,0,1]]
    Tz2 = matrix_product_p(Tz1,Tz1)
    Tz3 = matrix_product_p(Tz2,Tz1)
    _Tz1 = copy.deepcopy(Tz3)
    _Tz2 = copy.deepcopy(Tz2)
    _Tz3 = copy.deepcopy(Tz1)


    color_space = ['W','Y','B','G','O','R','P']
    color_show = ['white','yellow2','blue2','green','coral','red','none']

    position = [[ 1, 1,-1],[ 0, 1,-1],[-1, 1,-1],
                [ 1, 0,-1],[ 0, 0,-1],[-1, 0,-1],
                [ 1,-1,-1],[ 0,-1,-1],[-1,-1,-1],
                [ 1, 1, 0],[ 0, 1, 0],[-1, 1, 0],
                [ 1, 0, 0],[ 0, 0, 0],[-1, 0, 0],
                [ 1,-1, 0],[ 0,-1, 0],[-1,-1, 0],
                [ 1, 1, 1],[ 0, 1, 1],[-1, 1, 1],
                [ 1, 0, 1],[ 0, 0, 1],[-1, 0, 1],
                [ 1,-1, 1],[ 0,-1, 1],[-1,-1, 1]]

    oriention = [['OBW',[ i, j,_k]],['PBW',[ i, j,_k]],['RBW',[_i, j,_k]],
                 ['OPW',[ i, j,_k]],['PPW',[ i, j,_k]],['RPW',[_i, j,_k]],
                 ['OGW',[ i,_j,_k]],['PGW',[ i,_j,_k]],['RGW',[_i,_j,_k]],
                 ['OBP',[ i, j, k]],['PBP',[ i, j, k]],['RBP',[_i, j,_k]],
                 ['OPP',[ i, j, k]],['PPP',[ i, j, k]],['RPP',[_i, j, k]],
                 ['OGP',[ i,_j, k]],['PGP',[ i,_j, k]],['RGP',[_i,_j,_k]],
                 ['OBY',[ i, j, k]],['PBY',[ i, j, k]],['RBY',[_i, j, k]],
                 ['OPY',[ i, j, k]],['PPY',[ i, j, k]],['RPY',[_i, j, k]],
                 ['OGY',[ i,_j, k]],['PGY',[ i,_j, k]],['RGY',[_i,_j, k]]]

    cubeArray = list()
    for t in range(len(position)):
        cubeArray.append(cube(position[t],oriention[t][0],oriention[t][1]))

def location_transition(block,vec):
    'return the new cube'
    l = block.location
    v = vec
    new_l = matrix_product(v,l)
    block.location = new_l
    return block

def color_transition(block,vec):
    'return the new cube'
    global i,j,k
    c = block.color
    d = block.direction
    v = vec
    normal_order = [i,j,k]
    mirror = list()
    exchange = list()
    
    for temp in range(len(d)) :
        if d[temp] != normal_order[temp]:
            mirror.append(temp)
    new_d = matrix_product(v,normal_order)
    for temp in range(len(new_d)): # Mirror agian
        if temp in mirror:
            new_d[temp].reverse()
        if temp == 0 and (new_d[temp] not in [i,_i]):
            exchange.append(temp)
        elif temp == 1 and (new_d[temp] not in [j,_j]):
            exchange.append(temp)
        elif temp == 2 and (new_d[temp] not in [k,_k]):
            exchange.append(temp)

    if len(exchange) != 0:

        p = exchange[0]
        q = exchange[1]
        new_c = c[:p]+c[q]+c[p+1:q]+c[p]+c[q+1:]

        temp = new_d[p]
        new_d[p] = new_d[q]
        new_d[q] = temp

    block.color = new_c
    block.direction = new_d
    return block

def rotation(instruction,num):
    global cubeArray
    x = [Tx1,Tx2,Tx3,_Tx1,_Tx2,_Tx3]
    y = [Ty1,Ty2,Ty3,_Ty1,_Ty2,_Ty3]
    z = [Tz1,Tz2,Tz3,_Tz1,_Tz2,_Tz3]
    operation_range = list()
    if instruction.endswith('x'):
        if instruction.startswith('-'):
            for temp in range(len(cubeArray)):
                if cubeArray[temp].location[0] == -1:
                    operation_range.append(temp)

            for index in operation_range:
                block = cubeArray[index]
                block=location_transition(block,x[num-1])
                cubeArray[index]=color_transition(block,x[num+2])
##            return cubeArray
            
        else:
            for temp in range(len(cubeArray)):
                if cubeArray[temp].location[0] == 1:
                    operation_range.append(temp)

            for index in operation_range:
                block = cubeArray[index]
                block=location_transition(block,x[num+2])
                cubeArray[index]=color_transition(block,x[num-1])
##            return cubeArray
    elif instruction.endswith('y'):
        if instruction.startswith('-'):
            for temp in range(len(cubeArray)):
                if cubeArray[temp].location[1] == -1:
                    operation_range.append(temp)

            for index in operation_range:
                block = cubeArray[index]
                block=location_transition(block,y[num-1])
                cubeArray[index]=color_transition(block,y[num+2])
##            return cubeArray
            
        else:
            for temp in range(len(cubeArray)):
                if cubeArray[temp].location[1] == 1:
                    operation_range.append(temp)

            for index in operation_range:
                block = cubeArray[index]
                block=location_transition(block,y[num+2])
                cubeArray[index]=color_transition(block,y[num-1])
##            return cubeArray
    elif instruction.endswith('z'):
        if instruction.startswith('-'):
            for temp in range(len(cubeArray)):
                if cubeArray[temp].location[2] == -1:
                    operation_range.append(temp)

            for index in operation_range:
                block = cubeArray[index]
                block=location_transition(block,z[num-1])
                cubeArray[index]=color_transition(block,z[num+2])
##            return cubeArray
            
        else:
            for temp in range(len(cubeArray)):
                if cubeArray[temp].location[2] == 1:
                    operation_range.append(temp)

            for index in operation_range:
                block = cubeArray[index]
                block=location_transition(block,z[num+2])
                cubeArray[index]=color_transition(block,z[num-1])
##            return cubeArray
    else:
        print('Please input a formal instruction.')
    redraw()
    return cubeArray

def redraw():

    for c in cubeArray:
        l = c.location
        if l[0] == 1 or l[1] == 1 or l[2] == 1:
            if l[0] == 1:
                new_color = colorChange(c.color[0])
##                print(new_color)
                y_coord = l[1]+1
                z_coord = -l[2]+1
                coord = Initial_x+(gap+size)*y_coord,Initial_y+(gap+size)*z_coord,\
                        Initial_x+(gap+size)*y_coord+size,Initial_y+(gap+size)*z_coord,\
                        Initial_x+(gap+size)*y_coord+size,Initial_y+(gap+size)*z_coord+size,\
                        Initial_x+(gap+size)*y_coord,Initial_y+(gap+size)*z_coord+size

                exec('C.delete("front_%s_%s")'%(y_coord,z_coord))
                exec('front_%s_%s = C.create_polygon(coord, fill=new_color, tag="front_%s_%s")'%(y_coord,z_coord,y_coord,z_coord))
                
            if l[1] == 1:
                new_color = colorChange(c.color[1])
                x_coord = -l[0]+1
                z_coord = -l[2]+1

                coord = Initial_x+2*gap+3*size+(new_gap+new_size)*x_coord, Initial_y-(new_gap+new_size)*x_coord+(gap+size)*z_coord,\
                        Initial_x+2*gap+3*size+(new_gap+new_size)*x_coord+new_size, Initial_y-(new_gap+new_size)*x_coord+(gap+size)*z_coord-new_size,\
                        Initial_x+2*gap+3*size+(new_gap+new_size)*x_coord+new_size, Initial_y-(new_gap+new_size)*x_coord+(gap+size)*z_coord-new_size+size,\
                        Initial_x+2*gap+3*size+(new_gap+new_size)*x_coord, Initial_y-(new_gap+new_size)*x_coord+(gap+size)*z_coord+size
                exec('C.delete("right_%s_%s")'%(x_coord,z_coord))
                exec('right_%s_%s = C.create_polygon(coord, fill=new_color, tag="right_%s_%s")'%(x_coord,z_coord,x_coord,z_coord))

            if l[2] == 1:
                new_color = colorChange(c.color[2])
                y_coord = l[1]+1
                x_coord = -l[0]+1
                coord = Initial_x+(gap+size)*y_coord+(new_gap+new_size)*x_coord,Initial_y-(new_gap+new_size)*x_coord,\
                        Initial_x+(gap+size)*y_coord+(new_gap+new_size)*x_coord+size,Initial_y-(new_gap+new_size)*x_coord,\
                        Initial_x+(gap+size)*y_coord+(new_gap+new_size)*x_coord+size+new_size,Initial_y-(new_gap+new_size)*x_coord-new_size,\
                        Initial_x+(gap+size)*y_coord+(new_gap+new_size)*x_coord+size+new_size-size,Initial_y-(new_gap+new_size)*x_coord-new_size
                exec('C.delete("up_%s_%s")'%(y_coord,x_coord))
                exec('up_%s_%s = C.create_polygon(coord, fill=new_color, tag="up_%s_%s")'%(y_coord,x_coord,y_coord,x_coord))
                
    C.update()

def colorChange(input):
    if input == 'W':
        return 'white'
    elif input == 'Y':
        return 'yellow2'
    elif input == 'B':
        return 'blue2'
    elif input == 'G':
        return 'green'
    elif input == 'O':
        return 'coral'
    elif input == 'R':
        return 'red'
    else:
        return None
initialize()


color_space = ['W','Y','B','G','O','R','P']
color_show = ['white','yellow2','blue2','green','coral','red','none']

size = 60
Initial_x=70
Initial_y=120
gap = 8
root = Tk()
root.geometry('500x400')
C = Canvas(root, bg ='gray', height=400, width=400, scrollregion=(0,0,400,400))
C.place(x=0,y=0)

initial_y = Initial_y
for row in range(3):#z-axis
    initial_x = Initial_x
    for column in range(3):#y-axis

        coord = initial_x, initial_y, initial_x+size, initial_y,\
                initial_x+size, initial_y+size, initial_x, initial_y+size

        exec('front_%s_%s = C.create_polygon(coord, fill="coral", tag="front_%s_%s")'%(row,column,row,column))
        initial_x = initial_x + size + gap
    initial_y = initial_y + size +gap
    
initial_y = Initial_y
initial_x = Initial_x
new_size = (size/2)/(2**0.5)
new_gap = (gap/2)/(2**0.5)
for row in range(3):#x-axis
    for column in range(3):#y-axis
        coord = initial_x, initial_y, initial_x+size, initial_y,\
                initial_x+size+new_size, initial_y-new_size, initial_x+new_size, initial_y-new_size
        exec('up_%s_%s = C.create_polygon(coord, fill="yellow2",tag="up_%s_%s")'%(row,column,row,column))
        initial_x = initial_x + size + gap
    initial_x = Initial_x + (new_size + new_gap)*(row+1)
    initial_y = Initial_y - (new_size + new_gap)*(row+1)

initial_y = Initial_y
initial_x = Initial_x + 2*gap + 3*size
for row in range(3):#x-axis
    for column in range(3):#z-axis
        coord = initial_x, initial_y, initial_x, initial_y+size,\
                initial_x+new_size, initial_y+size-new_size, initial_x+new_size, initial_y-new_size
        exec('right_%s_%s = C.create_polygon(coord, fill="blue2",tag="right_%s_%s")'%(row,column,row,column))
        initial_x = initial_x+new_gap+new_size
        initial_y = initial_y-new_gap-new_size
    initial_x = Initial_x + 2*gap + 3*size
    initial_y = Initial_y + (size+gap)*(row+1)

xbutton = Button(root,text='x1',command = lambda:rotation('x',1))
xbutton.place(x=402,y=0,height=50,width=100)
_xbutton = Button(root,text='-x1',command = lambda:rotation('-x',1))
_xbutton.place(x=402,y=50,height=50,width=100)

ybutton = Button(root,text='|\n﹀',bg='gray',relief = 'groove',command = lambda:rotation('y',1))
ybutton.place(x=212,y=320,height=60,width=50)
_ybutton = Button(root,text='︿\n|',bg='gray',relief = 'groove',command = lambda:rotation('-y',1))
_ybutton.place(x=76,y=320,height=60,width=50)

zbutton = Button(root,text='-->',bg='gray',relief = 'groove',command = lambda:rotation('z',1))
zbutton.place(x=10,y=130,height=50,width=60)
_zbutton = Button(root,text='<--',bg='gray',relief = 'groove',command = lambda:rotation('-z',1))
_zbutton.place(x=10,y=265,height=50,width=60)
##C.update()


root.mainloop()
##a=[[1, 0, 0],
##   [0, 0, 1],
##   [0,-1, 0]]
##b=[i,j,k]
##print(matrix_product(a,b))


