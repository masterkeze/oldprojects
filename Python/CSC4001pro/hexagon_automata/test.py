# Test of cell.py

#from Cell import *
from tkinter import *

def get_coord(x,y,r):
    # input the real coordinate of the center
    x1 = x - r
    y1 = y
    x2 = x - 0.5*r
    y2 = y + 3**0.5/2*r
    x3 = x + 0.5*r
    y3 = y2
    x4 = x + r
    y4 = y
    x5 = x3
    y5 = y - 3**0.5/2*r
    x6 = x2
    y6 = y5
    return x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6

def get_center(x,y,r,base_x=0,base_y=0):
    # input the index of cell x and y.
    # r is the radius of the hexagon
    v1_x = 3/2 * r
    v1_y = 3**0.5/2 * r
    v2_x = 0
    v2_y = -3**0.5 * r

    real_x = x * v1_x
    real_y = x * v1_y + y * v2_y
    return real_x + base_x, real_y + base_y

def draw_hex(x,y,r,gap=0.2):
    coord = get_coord(x,y,r-int(r*gap))
    C.create_polygon(coord,outline="gold2",fill="alice blue")

def draw_cell(x,y,r,gap=0.2):
    coord = get_coord(x,y,r-int(r*gap))
    C.create_polygon(coord ,fill="SteelBlue1")

def get_neighbor(x,y):
    return [(x+1,y),(x+1,y+1),(x,y+1),(x-1,y),(x-1,y-1),(x,y-1)]
    
def span(x,y,r,base_x,base_y):
    visit = list()
    visited = list()
    visit.append((x,y))
    while visit != []:
        x,y = visit.pop(0)
        visited.append((x,y))
        real_x,real_y = get_center(x,y,r,base_x,base_y)
        #print(real_x,real_y)
        if real_x < -1*r or real_x > canvas_width + r or real_y < -1*r or real_y >canvas_height + r:
            continue
        if (x,y) == (0,0):
            draw_cell(real_x,real_y,r)
        else:
            draw_hex(real_x,real_y,r)
        temp = get_neighbor(x,y)
        for i in temp:
            if not(i in visit) and not(i in visited):
                visit.append(i)

def fill_canvas(r,base_x=0,base_y=0):
    if base_x >= 0 and base_y >=0 \
       and base_x <= canvas_width and base_y <= canvas_height:
        span(0,0,r,base_x,base_y)
    else:
        x_index = int((0.5*canvas_width - base_x)/(3/2*r))
        y_index = int((0.5*canvas_height - base_y - x_index*3**0.5/2*r)/(-3**0.5*r))
        span(x_index,y_index,r,base_x,base_y)

def click_b3(event):
    # print("click")
    global B3_holding, B3_x, B3_y
    B3_holding = True
    B3_x = event.x
    B3_y = event.y
    # print(base_x, base_y)
    return None


def hold_b3(event):
    if not B3_holding:
        return None
    global B3_x, B3_y, base_x, base_y
    diff_x = event.x - B3_x
    diff_y = event.y - B3_y
    base_x += diff_x
    base_y += diff_y
    B3_x = event.x
    B3_y = event.y
    if (diff_x ** 2 + diff_y ** 2) > 2:
        C.delete("all")
        fill_canvas(radius,base_x,base_y)
    # print(diff_x,diff_y)
    # print("Mouse position: (%s, %s)" % (event.x,event.y))
    # print("Base position: (%s, %s)" % (base_x, base_y))
    return None


def release_b3(event):
    # print("release")
    global B3_holding
    B3_holding = False
    return None


def leave(event):
    global B3_holding
    B3_holding = False
    return None

global root, C
global B3_holding, B3_x, B3_y, base_x, base_y

B3_holding = False
B3_x = -1
B3_y = -1
base_x = 0
base_y = 0

window_height = 600
window_width = 800
canvas_height = 9 / 10 * window_height
canvas_width = 3 / 4 * window_width

radius = 30

root = Tk()
root.title('Demo')
root.geometry('%sx%s' % (window_width + 60, window_height))
C = Canvas(root, bg='alice blue', height=canvas_height, width=canvas_width)
C.place(x=0, y=window_height - canvas_height)

C.bind('<Button-3>', click_b3)
C.bind('<B3-Motion>', hold_b3)
C.bind('<ButtonRelease-3>', release_b3)
#C.bind('<Leave>',release_b3)

fill_canvas(radius)
root.mainloop()
