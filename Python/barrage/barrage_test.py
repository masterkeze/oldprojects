from tkinter import *
import random,time,math

height = 400
width = 600

root = Tk()
root.title('Barrage test')
root.geometry('%sx%s+100+100'%(width,height))

C = Canvas(root, bg='gray', height=height,width=width)
C.place(x=-2,y=-2)

class bullet():
    def __init__(self, diameter = 5, x=width/2, y=height/2, direction = 0, speed = 2.5, tag="default", color="blue"):
        self.diameter = diameter
        self.radius = self.diameter/2
        
        self.x = x
        self.y = y
        self.coord = self.x-self.radius, self.y-self.radius,\
                     self.x+self.radius, self.y+self.radius

        self.direction = direction
        self.speed = speed

        self.tag = tag
        self.color = color

        C.create_oval(self.coord, fill = self.color, outline = self.color, tag = self.tag)
        C.update()


    def keep_going(self):
        C.delete(self.tag)
        angle = self.direction*math.pi/180
        self.x = self.x + math.cos(angle)*self.speed
        self.y = self.y + math.sin(angle)*self.speed
        
        self.coord = self.x-self.radius, self.y-self.radius,\
                     self.x+self.radius, self.y+self.radius
        
        if self.x > 0 and self.x < width and self.y > 0 and self.y < height:
            C.create_oval(self.coord, fill = self.color, outline = self.color, tag = self.tag)
            C.update()
            #print("moving")
            return True
        else:
            return False
        


center = bullet(15,width/2,height/2,0,0,"default","white")
sharpnel = 4
angle = 0
angular_vec = 10
angular_acc = 0.1
update_list = list()
for t in range(5000):
    if (t%5 == 0):
        angle = angle + angular_vec
        angular_vec = angular_vec + angular_acc
        for n in range(sharpnel):
            exec("bullet%s_%s = bullet(5,width/2,height/2,angle+n*360/sharpnel,2.5,\"bullet%s_%s\")"%(t,n,t,n))
            exec("update_list.append(bullet%s_%s)"%(t,n))
    index = 0
    while(len(update_list) > index):
        flag = update_list[index].keep_going()
        if flag:
            index = index + 1;
        else:
            update_list.pop(index)
    time.sleep(0.0166)










        
