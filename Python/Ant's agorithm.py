from tkinter import *
import random,time,math

height = 600
width = 800
radius = 2.5
velocity = 2

root = Tk()
root.title('Ant\'s agroithm')
root.geometry('%sx%s+100+100'%(width,height))
C = Canvas(root, bg='gray', height=height,width=width)
C.place(x=-2,y=-2)


class ant():
    def __init__(self,tag="0",color="red",x=400,y=300):
        self.x = x
        self.y = y
        self.tag = tag
        self.color = color
        self.angle = random.random()*math.pi*2
        self.direction = [math.cos(self.angle),math.sin(self.angle)]
        self.coord = self.x-radius,self.y-radius,self.x+radius,self.y+radius
        C.create_oval(self.coord,fill=self.color,outline=self.color,tag=self.tag)
        C.update()
    def random_walk(self):
        C.delete(self.tag)
        if self.x < 20 :
            self.angle = (random.random()-0.5)*math.pi/5
            print('changed')
            
        if self.y < 20:
            self.angle = math.pi*1/2+(random.random()-0.5)*math.pi/5
            print('changed')

        if self.x > width-20:
            self.angle = math.pi+(random.random()-0.5)*math.pi/5
            print('changed')
            

        if self.y > height-20:
            self.angle = math.pi*3/2+(random.random()-0.5)*math.pi/5
            print('changed')
            
        self.x = self.x + self.direction[0]*velocity
        self.y = self.y + self.direction[1]*velocity
        temp = (random.random()-0.5)*math.pi/10

        self.angle = self.angle + temp
        self.direction = [math.cos(self.angle),math.sin(self.angle)]
        self.coord = self.x-radius,self.y-radius,self.x+radius,self.y+radius
        C.create_oval(self.coord,fill=self.color,outline=self.color,tag=self.tag)
        C.update()

COLOR=["blue","red","green","gold"]
for num in range(100):
    c = COLOR[0]
    print("ant_%s = ant(\"ant_%s\",\"%s\")"%(num,num,str(c)))
    exec("ant_%s = ant(\"ant_%s\",\"%s\")"%(num,num,str(c)))
for t in range(5000):
    for num in range(100):
        exec("ant_%s.random_walk()"%(num))
    C.update()
    time.sleep(0.03)
