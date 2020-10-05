import Square
import Helper

import copy

class Cube():
    def __init__(self, default = True, id = -1):
        self.cube  = [Square.Square(1),
                    Square.Square(2), 
                    Square.Square(3), 
                    Square.Square(4), 
                    Square.Square(5), 
                    Square.Square(6)]
        self.queueReady = False
        self.sides = 6
        self.id = id

    def getID(self):
        return self.id

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

    def getPositionArray(self):
        return [self.cube[0].getPos(),
                self.cube[1].getPos(),
                self.cube[2].getPos(),
                self.cube[3].getPos(),
                self.cube[4].getPos(),
                self.cube[5].getPos()]

    def swapQueue(self, cube):
        if self.queueReady:
            print("Warning: This cube already has a pair {}".format(self.getCords()))
            
        if type(cube) == Cube and self.sides == cube.getNumberOfSides():
            self.queue = cube.getPositionArray()
            self.queueID = cube.getID()
            self.queueReady = True
        else:
            print("Either object was not a cube or sides missmatch")

    def swapCommitQueue(self):
        if not self.queueReady:
            #print("Warning: This cube is not ready to swap {}".format(self.getCords()))
            return
        self.setSide(0, self.queue[0])
        self.setSide(1, self.queue[1])
        self.setSide(2, self.queue[2])
        self.setSide(3, self.queue[3])
        self.setSide(4, self.queue[4])
        self.setSide(5, self.queue[5])
        self.setID(self.queueID)
        self.queue = []
        self.queueReady = False

    def queueState(self):
        return self.queueReady

    def rotateCube(self, plain: int, reverse: bool):
        temp = self.getPositionArray()
        if (plain == 0):
            if reverse:
                self.cube[0] = Square.Square(temp[2])
                self.cube[1] = Square.Square(temp[3])
                self.cube[2] = Square.Square(temp[1])
                self.cube[3] = Square.Square(temp[0])
            else:
                self.cube[0] = Square.Square(temp[3])
                self.cube[1] = Square.Square(temp[2])
                self.cube[2] = Square.Square(temp[0])
                self.cube[3] = Square.Square(temp[1])
        elif (plain == 1):
            if reverse:
                self.cube[2] = Square.Square(temp[4])
                self.cube[3] = Square.Square(temp[5])
                self.cube[4] = Square.Square(temp[3])
                self.cube[5] = Square.Square(temp[2])
            else:
                self.cube[2] = Square.Square(temp[5])
                self.cube[3] = Square.Square(temp[4])
                self.cube[4] = Square.Square(temp[2])
                self.cube[5] = Square.Square(temp[3])
        else:
            if reverse:
                self.cube[0] = Square.Square(temp[4])
                self.cube[1] = Square.Square(temp[5])
                self.cube[4] = Square.Square(temp[1])
                self.cube[5] = Square.Square(temp[0])
            else:
                self.cube[0] = Square.Square(temp[5])
                self.cube[1] = Square.Square(temp[4])
                self.cube[4] = Square.Square(temp[0])
                self.cube[5] = Square.Square(temp[1])

    def setID(self, id):
        self.id = id

    def setSide(self, side: int, color: int):
        self.cube[side] = Square.Square(color)

    def setSideOverride(self, side: int, color: int):
        self.cube[side].setColorOverride(color)

    def setSideSquare(self, side: int, square: Square):
        print("Deprecated:Do not call setSideSqaure")
        self.cube[side] = copy.deepcopy(square)
    
    def removeSide(self, side):
        self.cube[side].setColor(0)
        self.cube[side].setPos(0)
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
        print("Deprecated: Do not call creatCopy")
        return copy.deepcopy(self)
    
    def __str__(self):
        return "South:{},\nNorth:{},\nTop:{},\nBottom:{},\nWest:{},\nEast:{}".format(self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5])