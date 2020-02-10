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
        else:
            pass

    def addSide(self, side, color):
        self.cube[side] = Square.Square(side, color)
    
    def removeSide(self, side):
        self.cube[side].setColor(6)

    def getCube(self):
        return self.cube

    def getSquare(self, side): 
        return self.cube[side]
    
    def createCopy(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return "West:{},\nSouth:{},\nNorth:{},\nEast:{},\nTop:{},\nBottom:{}".format(self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5])