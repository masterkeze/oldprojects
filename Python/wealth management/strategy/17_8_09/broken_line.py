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

def difference(line1,line2,date_option == False):
    if type(line1) == broken_line and type(line2) == broken_line\
       and type(date_option) == bool:
        if (date_option):
            ######################################
        else:
            outcome = broken_line()
            length = min(line1.length,line2.length)
            if length == 0:
                print("Empty input")
                return None
            
            title = str(line1.points[0].title)+' - '+str(line2.points[0].title)
            date = "Unknown"
            for t in range(length):
                value = line1.points[t].value - line2.points[t].value
                outcome.add_point(title,date,value)
            return outcome
        
    else:
        print("Wrong input of difference(line1,line2)")
        return None
