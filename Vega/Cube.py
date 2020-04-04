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

    # Column rotate clockwise
    # east & west stay the same
    # Top    > North
    # North  > Bottom
    # Bottom > south
    # South  > top
    # counter Clockwise of above is reverse of above

    # Row rotate Clockwise
    # Top & bottom stay the same
    # North > east
    # east  > south
    # south > west
    # west  > north
    # counter Clockwise is the reverse of above
    #West > sount > north > east > top > bottom

    #self.setSide(0,self.getSquare(0).getColor()) #west
    #self.setSide(1, self.getSquare(5).getColor()) #south
    #self.setSide(2, self.getSquare(4).getColor()) #north
    #self.setSide(3,self.getSquare(0).getColor()) #east
    #self.setSide(4, self.getSquare(1).getColor()) #top
    #self.setSide(5, self.getSquare(2).getColor()) #bottom 
    #0:"West"
    #1:"South"
    #2:"North"
    #3:"East"
    #4:"Top"
    #5:"Bottom"

    def rotateCube(self, plain: int, reverse: bool):
        temp = copy.deepcopy(self.cube)
        if (plain == 0):
            if reverse:#Counter-clockwise
                self.cube[1] = temp[4]
                self.cube[2] = temp[5]
                self.cube[4] = temp[2]
                self.cube[5] = temp[1]
            else:#clockwise
                self.cube[1] = temp[5]
                self.cube[2] = temp[4]
                self.cube[4] = temp[1]
                self.cube[5] = temp[2]
        elif (plain == 1):
            pass
        else:
            pass

    def setSide(self, side: int, color: int):
        self.cube[side] = Square.Square(side, color)

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
        #self.cube[side].setSide(square.getSide())
    
    def createCopy(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return "West:{},\nSouth:{},\nNorth:{},\nEast:{},\nTop:{},\nBottom:{}".format(self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5])