class Cell:
    def __init__(self,x,y,ground):
        
        self.x = x
        self.y = y
        self.mode = 0
        self.nextMode = 0
        self.neighbor = dict()
        self.ground = ground
        ground.cells[(x,y)] = self

        self.addNeighbor()

    def getPos(self,index):
        #index is the position of the new cell
        #2 o'clock is labeled 0 and 4 o'clock labeled 1
        if index == 0:
            x = self.x + 1
            y = self.y + 1
        elif index == 1:
            x = self.x
            y = self.y + 1
        elif index == 2:
            x = self.x - 1
            y = self.y
        elif index == 3:
            x = self.x - 1
            y = self.y - 1
        elif index == 4:
            x = self.x
            y = self.y - 1
        elif index == 5:
            x = self.x + 1
            y = self.y - 1

        return (x,y)

    def addNeighbor(self):
        for i in range(6):
            p = self.getPos(i)
            if self.ground.cells.get(p, -1) != -1:
                self.neighbor[i] = self.ground.cells[p]
                self.neighbor[i].neighbor[i-3] = self

    def expand(self,index):
        p = self.getPos(index)
        c = Cell(p[0], p[1], self.ground)

        return c

    def getNext(self,lifeList,spawnList):
        n = 0
        for i in range(6):
            if self.neighbor.get(i,0) == 1:
                n = n + 1

        if (self.mode == 1) and (n in lifeList):
            self.nextMode = 1
        elif (self.mode == 0) and (n in spawnList):
            self.nextMode = 1
        else:
            self.nextMode = 0

        return self.nextMode

    def upgrade(self):
        self.mode = self.nextMode
        if self.mode == 1:
            for i in range(6):
                if self.neighbor.get(i,-1) == -1:
                    self.expand(i)
        self.nextMode = 0


class Ground:
    def __init__(self):
        self.cells = dict()
        self.lives = list()

        self.cells[(0,0)] = Cell(0, 0, self)

    def addCell(self,x,y):
        if self.cells.get((x,y),-1) == -1:
            self.cells[(x,y)] = Cell(x, y, self)
            return self.cells[(x,y)]
        else:
            return "position taken"

    def switchMode(self,x,y):
        c = self.cells.get((x,y),-1)
        if c == -1:
            c = self.addCell(x,y)
            
        if c.mode == 0:
            c.mode == 1
            c.upgrade()
        elif c.mode == 1:
            c.mode == 0

        self.getLives()

    def getLives(self):
        self.lives = list()
        for i in self.cells.values():
            if i.mode == 1:
                self.lives.append(i)

    def evolve(self,lifeList,spawnList):
        checked = list()
        for i in self.lives:
            if i not in checked:
                i.getNext(lifeList,spawnList)
            for j in range(6):
                t = i.neighbor[j]
                if t not in checked:
                    checked.append(t)
                    t.getNext(lifeList,spawnList)

        for i in checked:
            i.upgrade()

        self.getLives()

        
                
                
