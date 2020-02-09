import Square
import Helper

import copy

class Cube():
    def __init__(self, default):
        if default == True:
            self.cube  = [Square.Square(Helper.helper.sideDictRev[0], Helper.helper.colorDictRev[0]),
            Square.Square(Helper.helper.sideDictRev[1], Helper.helper.colorDictRev[1]), 
            Square.Square(Helper.helper.sideDictRev[2], Helper.helper.colorDictRev[2]), 
            Square.Square(Helper.helper.sideDictRev[3], Helper.helper.colorDictRev[3]), 
            Square.Square(Helper.helper.sideDictRev[4], Helper.helper.colorDictRev[4]), 
            Square.Square(Helper.helper.sideDictRev[5], Helper.helper.colorDictRev[5])]
        else:
            pass

    def addSide(self, side, color):
        self.cube[Helper.helper.sideDict[side]] = Square.Square(side, color)
    
    def removeSide(self, side):
        self.cube[Helper.helper.sideDict[side]].setColor(Helper.helper.colorDictRev[6])

    def getCube(self):
        return self.cube

    def getSquare(self, side): 
        return self.cube[Helper.helper.sideDict[side]]
    
    def createCopy(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return "West:{},\nSouth:{},\nNorth:{},\nEast:{},\nTop:{},\nBottom:{}".format(self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5])