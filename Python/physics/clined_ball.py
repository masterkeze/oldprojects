from tkinter import *
import random, time, math
global fps, interval, meter, height, width, friction_coefficient, root, C
global gravity, acc, gravity_record
gravity = [0,0] #[scalar, direction]
gravity_record=[]
acc = 300
fps = 60
interval = 1/fps
meter = 30 #1 meter = ? pixel
height = 600
width = 900
friction_coefficient = 0

walls = [[(80,80),(width-80,80)],[(80,80),(80,height-80)],\
         [(width-80,80),(width-80,height-80)],[(80,height-80),(width-80,height-80)]]



root = Tk()
root.title('Inclined Ball')
root.geometry('%sx%s+100+50'%(width,height))

C = Canvas(root, bg='alice blue', height=height,width=width)
C.place(x=0,y=0)

def get_angle(x,y):
    s = math.sqrt(x**2+y**2)
    if s == 0:
        return 0
    else:
        angle = (math.asin(y/s)/math.pi*180)%360
        if x < 0:
            return round(180 - angle,3)
        else:
            return round(angle,3)

def distance(line,x,y):
    p1 = line[0]
    p2 = line[1]
    A = p2[1] - p1[1]
    B = p1[0] - p2[0]
    C = p2[0]*p1[1] - p1[0]*p2[1]
    if p1 == p2 and p1 == 0:
        print('Invalid wall')
        return None
    else:
        return abs((A*x+B*y+C)/math.sqrt(x**2+y**2))
    
def collision(x,y,r):
    for wall in walls:
        if distance(wall,x,y) <= r:
            tempx = wall[1][0] - wall[0][0]
            tempy = wall[1][1] - wall[0][1]
            direction = get_angle(tempx,tempy)
            return direction
    return None

class ball():
    def __init__(self, mass = 1, radius = 1, position = [width/2,height/2],\
                 velocity = 0, direction = 0, tag = "ball"):
        self.mass = mass
        self.radius = radius
        self.diameter = self.radius*2
        self.position = position
        self.velocity = velocity
        self.direction = direction
        self.angle = self.direction*math.pi/180
        self.v_x = math.cos(self.angle)*self.velocity
        self.v_y = math.sin(self.angle)*self.velocity
        self.tag = tag

    def set_velocity(self,velocity,direction):
        self.velocity = velocity
        self.direction = direction
        self.angle = self.direction*math.pi/180
        self.v_x = math.cos(self.angle)*self.velocity
        self.v_y = math.sin(self.angle)*self.velocity

    def add_velocity(self,velocity,direction):
        new_angle = direction*math.pi/180
        new_v_x = math.cos(new_angle)*velocity
        new_v_y = math.sin(new_angle)*velocity

        self.v_x = self.v_x + new_v_x
        self.v_y = self.v_y + new_v_y
        self.velocity = (self.v_x**2 + self.v_y**2)**0.5
        self.direction = get_angle(self.v_x,self.v_y)
        #print("add_velocity")

    def friction_impact(self):
        if self.velocity < 0.01:
            pass
        elif (friction_coefficient*self.mass*interval) > self.velocity :
            self.add_velocity(self.velocity,self.direction+180)
        else:
            self.add_velocity(friction_coefficient*self.mass*interval,self.direction+180)
        
    def global_impact(self):
        self.add_velocity(gravity[0]*interval,gravity[1])

    def update(self):
        if self.velocity < 0.01:
            self.reset()
        self.direction = self.direction%360
        self.friction_impact()
        self.global_impact()

        
        self.angle = self.direction/180*math.pi
        next_position = [self.position[0]+self.velocity*math.cos(self.angle)*interval,\
                         self.position[1]+self.velocity*math.sin(self.angle)*interval]

        mirror = collision(next_position[0],next_position[1],self.radius)
        if mirror != None:
            mirror = mirror%180
            self.direction = (2*mirror - self.direction)%360
            self.set_velocity(0.8*self.velocity,self.direction)
            self_position = [self.position[0]+self.velocity*math.cos(self.angle)*interval,\
                             self.position[1]+self.velocity*math.sin(self.angle)*interval]
        else:
            self.position = next_position
            
    def reset(self):
        self.velocity = 0
        self.direction = 0
        self.v_x = 0
        self.v_y = 0
        self.angle = 0        

def draw_walls():
    wall_height = 10
    for wall in walls:
        C.create_line(wall[0][0],wall[0][1],wall[1][0],wall[1][1])
        C.create_line(wall[0][0],wall[0][1],wall[0][0]-wall_height,wall[0][1]+wall_height)
        C.create_line(wall[0][0]-wall_height,wall[0][1]+wall_height,wall[1][0]-wall_height,wall[1][1]+wall_height)
        C.create_line(wall[1][0]-wall_height,wall[1][1]+wall_height,wall[1][0],wall[1][1])
        C.create_polygon(wall[0][0],wall[0][1],wall[1][0],wall[1][1],\
                         wall[1][0]-wall_height,wall[1][1]+wall_height,\
                         wall[0][0]-wall_height,wall[0][1]+wall_height,\
                         fill = 'yellow')
        C.update()

def draw_ball(B):
    global C
    x = B.position[0]
    y = B.position[1]
    r = B.radius
    coord = x-r,y-r,x+r,y+r
    if x>0 and y>0 and x< width and y < height:
        C.create_oval(coord,fill = 'gray54',outline = 'gray54', tag = B.tag)
        C.update()
        #print("ball updated")
        
def delete_ball(B):
    global C
    C.delete(B.tag)

def reset_gravity():
    global gravity
    gravity = [0,0]

def add_gravity(g=[0,0]):
    global gravity
    old_angle = gravity[1]*math.pi/180
    old_g_x = gravity[0]*math.cos(old_angle)
    old_g_y = gravity[0]*math.sin(old_angle)
    
    angle = g[1]*math.pi/180
    g_x = g[0]*math.cos(angle)
    g_y = g[0]*math.sin(angle)

    new_g_x = old_g_x + g_x
    new_g_y = old_g_y + g_y
    temp_scalar = math.sqrt(new_g_x**2+new_g_y**2)
    temp_direction = get_angle(new_g_x,new_g_y)
    gravity = [temp_scalar,temp_direction]

    if gravity[0] < 0.01:
        reset_gravity()

def Press_W(root):
    g_y = gravity[0]*math.sin(gravity[1]*math.pi/180)
    if not(270 in gravity_record):
        gravity_record.append(270)
        add_gravity([acc,270])
    
    
def Release_W(root):
    g_y = gravity[0]*math.sin(gravity[1]*math.pi/180)
    if 270 in gravity_record:
        gravity_record.remove(270)
        add_gravity([acc,90])



def Press_S(root):
    g_y = gravity[0]*math.sin(gravity[1]*math.pi/180)
    if not(90 in gravity_record):
        gravity_record.append(90)
        add_gravity([acc,90])
    
    
def Release_S(root):
    g_y = gravity[0]*math.sin(gravity[1]*math.pi/180)
    if 90 in gravity_record:
        gravity_record.remove(90)
        add_gravity([acc,270])



def Press_A(root):
    g_x = gravity[0]*math.cos(gravity[1]*math.pi/180)
    if not(180 in gravity_record):
        gravity_record.append(180)
        add_gravity([acc,180])
        
    
    
def Release_A(root):
    g_x = gravity[0]*math.cos(gravity[1]*math.pi/180)
    if 180 in gravity_record:
        gravity_record.remove(180)
        add_gravity([acc,0])
        

        

def Press_D(root):
    g_x = gravity[0]*math.cos(gravity[1]*math.pi/180)
    if not(0 in gravity_record):
        gravity_record.append(0)
        add_gravity([acc,0])
        
        
    
    
def Release_D(root):
    g_x = gravity[0]*math.cos(gravity[1]*math.pi/180)
    if 0 in gravity_record:
        gravity_record.remove(0)
        add_gravity([acc,180])
        


root.bind("<KeyPress-w>",Press_W)
root.bind("<KeyRelease-w>",Release_W)
root.bind("<KeyPress-s>",Press_S)
root.bind("<KeyRelease-s>",Release_S)
root.bind("<KeyPress-a>",Press_A)
root.bind("<KeyRelease-a>",Release_A)
root.bind("<KeyPress-d>",Press_D)
root.bind("<KeyRelease-d>",Release_D)

B = ball(1,0.5*meter,[400,height/2],meter)

draw_ball(B)
draw_walls()
##coord1 = 300-30,height/2-30,\
##         300+30,height/2+30
##C.create_oval(coord1,fill = 'red',outline = 'red', tag = "1")
##
##coord2 = 500-30,height/2-30,\
##         500+30,height/2+30
##C.create_oval(coord2,fill = 'red',outline = 'red', tag = "2")

for t in range(120):
    ##print("direction = ",round(B.direction,4))
    
    for frame in range(fps):
        B.update()
        delete_ball(B)
        draw_ball(B)
        time.sleep(interval)

root.mainloop()













    
