from point import *

class broken_line():

    def __init__(self,p = None):
        self.points = list()
        self.length = 0
        self.highest = -999999999999
        self.lowest = 999999999999
        if p != None and type(p) == point:
            self.points.append(p)
            self.length = self.length + 1
            self.highest = p.value
            self.lowest = p.value

    def add_point(self, p):
        if type(p) == point:
            self.points.append(p)
            self.length = self.length + 1
            if p.value > self.highest:
                self.highest = p.value
            if p.value < self.lowest:
                self.lowest = p.value
        else:
            print("Only point can be added.")

    def add_point(self, title, date, value):
        p = point(title,date,value)
        self.points.append(p)
        self.length = self.length + 1
        if p.value > self.highest:
            self.highest = p.value
        if p.value < self.lowest:
            self.lowest = p.value
