# This file is to plot points in the form of (x,y)

from tkinter import *

width = 500
height = 400

root = Tk()
root.title("Scattered Points")
root.geometry('%sx%s+300+50'%(width,height))

C = Canvas(root, bg='alice blue',height = height, width = width)
C.place(x=0,y=0)

def plot(points):
    gap = 60
    scatter_rate = 1.2
    x_split = int(width/100+0.5)
    y_split = int(height/100+0.5)
    x_l = None
    x_u = None
    y_l = None
    y_u = None
    count = 0
    for pair in points:
        if x_l == None:
            x_l = pair[0]
            x_u = pair[0]
            y_l = pair[1]
            y_u = pair[1]
        else:
            x_l = min(x_l,pair[0])
            x_u = max(x_u,pair[0])
            y_l = min(y_l,pair[1])
            y_u = max(y_u,pair[1])
        count = count + 1
    if count == 0:
        return 0
    if count == 1:
        points.append((0,0))
        plot(points)
        return 0
    else:
        x_center = (x_u+x_l)/2
        y_center = (y_u+y_l)/2
        x_scale = scatter_rate*(x_u-x_l)/x_split
        y_scale = scatter_rate*(y_u-y_l)/y_split
        x_stand = x_center-x_scale*x_split/2
        y_stand = y_center+y_scale*y_split/2
        # draw coord_line
        x_distance = (width - 2*gap)/x_split
        for i in range(x_split+1):
            C.create_line(gap+i*x_distance,gap,gap+i*x_distance,height-gap,fill='gray')
            #C.create_text(gap+i*x_distance,0.5*gap,text=str(round(x_stand+i*x_scale,2)))
            C.create_text(gap+i*x_distance,height-0.5*gap,text=str(round(x_stand+i*x_scale,2)))
        y_distance = (height - 2*gap)/y_split
        for j in range(y_split+1):
            C.create_line(gap,gap+j*y_distance,width-gap,gap+j*y_distance,fill='gray')
            C.create_text(0.5*gap,gap+j*y_distance,text=str(round(y_stand-j*y_scale,2)))
