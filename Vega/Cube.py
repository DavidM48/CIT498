import Square
import Helper

import copy

class Cube():
    def __init__(self, default):
        if default == True:
            self.cube  = [Square.Square(0, 0),
            Square.Square(1, 1), 
            Square.Square(2, 2), 
            Square.Square(3, 3), 
            Square.Square(4, 4), 
            Square.Square(5, 5)]
            self.queueReady = False
        else:
            pass
    
    def setCords(self, x, y, z):
        self.x = copy.deepcopy(x)
        self.y = copy.deepcopy(y)
        self.z = copy.deepcopy(z)
    
    def getCords(self):
        return [self.x, self.y, self.z]

    def swapQueue(self, cube):
        if type(cube) == Cube:
            c = copy.deepcopy(cube)
            self.queue = [c.getSquare(0),
                    c.getSquare(1),
                    c.getSquare(2),
                    c.getSquare(3),
                    c.getSquare(4),
                    c.getSquare(5)]
            self.queueReady = True

    def swapCommitQueue(self):
        if not self.queueReady:
            return
        self.setSquare(0, self.queue[0])
        self.setSquare(1, self.queue[1])
        self.setSquare(2, self.queue[2])
        self.setSquare(3, self.queue[3])
        self.setSquare(4, self.queue[4])
        self.setSquare(5, self.queue[5])
        self.queue = []
        self.queueReady = False

    def queueState(self):
        return self.queueReady
        
    def setSide(self, side, color):
        self.cube[side] = Square.Square(side, color)
    
    def removeSide(self, side):
        self.cube[side].setColor(6)

    def getCube(self):
        return self.cube

    def getSquare(self, side): 
        return self.cube[side]
    
    def setSquare(self, side, square: Square):
        self.cube[side].setColorHex(square.getColor())
        self.cube[side].setSide(square.getSide())
    
    def createCopy(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return "West:{},\nSouth:{},\nNorth:{},\nEast:{},\nTop:{},\nBottom:{}".format(self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5])