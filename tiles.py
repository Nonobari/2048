import random as rd

class Tiles:
    def __init__(self,x,y,flag = True) -> None:
        self.positionX = x
        self.positionY = y
        if flag:
            self.number = rd.choices([2,4],[0.8,0.2])[0]
        else: 
            self.number = 0
            
    def setPositionX(self,x):
        self.positionX = x