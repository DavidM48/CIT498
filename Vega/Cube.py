import Square
import Helper

import copy
import json

class Cube():
    def __init__(self, default):
        if default == True:
            self.cube  = [Square.Square(0),
                        Square.Square(1), 
                        Square.Square(2), 
                        Square.Square(3), 
                        Square.Square(4), 
                        Square.Square(5)]
            self.queueReady = False
            self.sides = 6
        else:
            pass
    
    def setCords(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def getCords(self):
        return [self.x, self.y, self.z]
    
    def getColorArray(self):
        return [self.cube[0].getColor(),
                self.cube[1].getColor(),
                self.cube[2].getColor(),
                self.cube[3].getColor(),
                self.cube[4].getColor(),
                self.cube[5].getColor()]

    def swapQueue(self, cube):
        if self.queueReady:
            print("Warning: This cube already has a pair {}".format(self.getCords()))
        if type(cube) == Cube and self.sides == cube.getNumberOfSides():
            c = copy.deepcopy(cube)
            self.queue = [c.getSquare(0),
                        c.getSquare(1),
                        c.getSquare(2),
                        c.getSquare(3),
                        c.getSquare(4),
                        c.getSquare(5)]
            self.queueReady = True
        else:
            print("Either object was not a cube or sides missmatch")

    def swapCommitQueue(self):
        if not self.queueReady:
            #print("Warning: This cube is not ready to swap {}".format(self.getCords()))
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

    #0 south
    #1 north
    #2 top
    #3 bottom
    #4 west
    #5 east

    # 2 false
    # 2 > 5
    # 3 > 4
    # 4 > 2
    # 5 > 3
    def rotateCube(self, plain: int, reverse: bool):
        temp = copy.deepcopy(self.cube)
        if (plain == 0):
            if reverse:
                self.cube[0] = temp[2]
                self.cube[1] = temp[3]
                self.cube[2] = temp[1]
                self.cube[3] = temp[0]
            else:
                self.cube[0] = temp[3]
                self.cube[1] = temp[2]
                self.cube[2] = temp[0]
                self.cube[3] = temp[1]
        elif (plain == 1):
            if reverse:
                self.cube[2] = temp[4]
                self.cube[3] = temp[5]
                self.cube[4] = temp[3]
                self.cube[5] = temp[2]
            else:
                self.cube[2] = temp[5]
                self.cube[3] = temp[4]
                self.cube[4] = temp[2]
                self.cube[5] = temp[3]
        else:
            if reverse:
                self.cube[0] = temp[4]
                self.cube[1] = temp[5]
                self.cube[4] = temp[1]
                self.cube[5] = temp[0]
            else:
                self.cube[0] = temp[5]
                self.cube[1] = temp[4]
                self.cube[4] = temp[0]
                self.cube[5] = temp[1]

    def setSide(self, side: int, color: int):
        self.cube[side] = Square.Square(color)

    def setSideOverride(self, side: int, color: int):
        self.cube[side].setColorOverride(color)

    def setSideSquare(self, side: int, square: Square):
        self.cube[side] = copy.deepcopy(square)
    
    def removeSide(self, side):
        self.cube[side].setColor(6)
        self.sides -= 1

    def getNumberOfSides(self):
        return self.sides

    def getCube(self):
        return self.cube

    def getSquare(self, side): 
        return self.cube[side]
    
    def setSquare(self, side, square: Square):
        self.cube[side].setColorHex(square.getColor())
    
    def createCopy(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return "South:{},\nNorth:{},\nTop:{},\nBottom:{},\nWest:{},\nEast:{}".format(self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5])