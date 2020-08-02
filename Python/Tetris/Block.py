def is_linked(vector1,vector2):
    difference = (vector1[0]-vector2[0],vector1[1]-vector2[1])
    choice = [(0,1),(0,-1),(1,0),(-1,0)]
    if difference in choice:
        return True
    else:
        return False

class Block():
    def __init__(self,initial):
        self.block = [initial]
        self.head = self.block[0]
        self.tail = self.block[len(self.block)-1]
        self.leftBound = initial[0]
        self.rightBound = initial[0]
        self.upBound = initial[1]
        self.downBound = initial[1]
        self.length = len(self.block)
        self.lowest = initial
        
    def add_block(self,vector):
        x = vector[0]
        y = vector[1]
        if is_linked(vector,self.tail) and not(vector in self.block):
            if y > self.downBound:
                self.lowest = vector
            self.block.append(vector)
            self.leftBound = min(self.leftBound,x)
            self.rightBound = max(self.rightBound,x)
            self.upBound = min(self.upBound,y)
            self.downBound = max(self.downBound,y)
            self.tail = vector
            self.length += 1
        else:
            pass
            #print('New block is unconnected to the old block.')
    def connect_block(self,vector):
        if vector not in self.block:
            self.block.append(vector)
            self.length + 1
            
    def delete_block(self,vector):
        if vector in self.block:
            del(self.block[self.block.index(vector)])
            self.length - 1

    def moveByVector(self,vector):
        newBlock = list()
        x = vector[0]
        y = vector[1]
        
        for i in range(self.length):
            temp = (self.block[i][0]+x,self.block[i][1]+y)
            newBlock.append(temp)
            
        self.block = newBlock
        self.leftBound += x
        self.rightBound += x
        self.upBound += y
        self.downBound += y
        self.lowest = (self.lowest[0]+x,self.lowest[1]+y)

    def addVector(self,vector):
        newBlock = list()
        x = vector[0]
        y = vector[1]
        
        for i in range(self.length):
            temp = (self.block[i][0]+x,self.block[i][1]+y)
            newBlock.append(temp)
            
        return newBlock

    def getBound(self):
        self.leftBound = None
        for i in self.block:
            x = i[0]
            y = i[1]
            if self.leftBound == None:
                self.leftBound = x
                self.rightBound = x
                self.upBound = y
                self.downBound = y
                self.lowest = i
            else:
                self.leftBound = min(self.leftBound,x)
                self.rightBound = max(self.rightBound,x)
                self.upBound = min(self.upBound,y)
                self.downBound = max(self.downBound,y)
                if y == self.downBound:
                    self.lowest = i
    
    def rotate(self,sign):
        'sign= 1:clockwise'
        'sign=-1:counter-clockwise'
        mid = (self.leftBound + self.rightBound)/2
        temp_block = list()
        temp_upBound = None
        for instance in self.block:
            temp_x = instance[0]
            temp_y = instance[1]
            new_x = sign*temp_y
            new_y = -1*sign*temp_x
            temp_block.append((new_x,new_y))
            if temp_upBound == None:
                temp_upBound = new_y
                temp_leftBound = new_x
                temp_rightBound = new_x
            else:
                temp_upBound = min(temp_upBound,new_y)
                temp_leftBound = min(temp_leftBound,new_x)
                temp_rightBound = max(temp_rightBound,new_x)
        temp_mid = (temp_leftBound + temp_rightBound)/2
        dif_y = int(self.upBound - temp_upBound)
        dif_x = int(mid - temp_mid)
        newBlock = list()
        for i in temp_block:
            temp_x = i[0]
            temp_y = i[1]
            new_x = temp_x + dif_x
            new_y = temp_y + dif_y
            newBlock.append((new_x,new_y))
        return newBlock

    def replace(self,newBlock):
        for i in self.block:
            self.delete_block(i)
        self.block = newBlock
        self.getBound()
        print('New block replaced.')
