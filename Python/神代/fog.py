# This file is trying to determing the best place for gods
# and the best strategy to attack
import numpy as np
class board():
    def __init__(self,god1,god2,god3):
        self.fog_init()
        self.gods = [god1,god2,god3]
        self.value_init()

    def fog_init(self):
        self.fog = np.reshape(np.zeros(16,int),(4,4))
        
    def value_init(self):
        self.value = np.reshape(np.ones(16,int),(4,4))
        for i in range(len(self.gods)):
            r = self.gods[i]//4
            c = self.gods[i]%4
            if i == 0:
                self.value[r][c] = 35
            else:
                self.value[r][c] = 17
            
    def hit(self,hits):
        for i in range(len(hits)):
            r = hits[i]//4
            c = hits[i]%4
            self.fog[r][c] = 1
        output = self.value * self.fog
        return output

def circle(center):
    output = list()
    output.append(center)
    if center//4 == (center + 1)//4:
        output.append(center + 1)
    if center+4 <= 15:
        output.append(center+4)
    if center+5 <= 15:
        output.append(center+5)
    return output

def cross(center):
    output = list()
    output.append(center)
    if center-4 >= 0:
        output.append(center-4)
    if (center-1)//4 == center//4:
        output.append(center-1)
    if (center+1)//4 == center//4:
        output.append(center+1)
    if center+4 <= 15:
        output.append(center+4)
    return output
