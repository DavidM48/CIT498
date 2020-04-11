import Cube
import Helper

import random
import math
import pprint
import copy

class Rubiks():
    
    def __init__(self, size):
        self.size = size
        self.logMoves = {}
        self.logCount = 0
        self.defaultCube()
        self.initRubiks()
        self.fillRubiks()
    
    def defaultCube(self):
        self.dc = Cube.Cube(True)

    def initRubiks(self):
        self.rubiks = [[[0 for col in range(self.size)] for col in range(self.size)] for row in range(self.size)] 

    def fillRubiks(self):
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    self.rubiks[x][y][z] = copy.deepcopy(self.dc)
                    self.rubiks[x][y][z].setCords(x, y, z)
                    # ! Doesn't work with cubes bigger than 3x3 !
                    if x <= 1:
                        self.rubiks[x][y][z].removeSide(0)
                    if x >= 1:
                        self.rubiks[x][y][z].removeSide(1)

                    if y <= 1:
                        self.rubiks[x][y][z].removeSide(2)
                    if y >= 1:
                        self.rubiks[x][y][z].removeSide(3)

                    if z <= 1:
                        self.rubiks[x][y][z].removeSide(4)
                    if z >= 1:
                        self.rubiks[x][y][z].removeSide(5)

    def getRubiks(self):
        return self.rubiks
    
    def getSize(self):
        return self.size

    def rotateRubiks(self, i: int, plain: int, reverse: bool):
        self.logMoves[self.logCount] = {"i":i,"plain":plain,"reverse":reverse}
        self.logCount = self.logCount + 1
        if (i >= self.size or i < 0):
            #Check to make sure i is within limits
            pass
        sliced = []

        #Fill the list with the cubes we need to swap
        for x in range(self.size):
            for y in range(self.size):
                if (plain == 0):
                    sliced.append((self.rubiks[x][y][i]))
                elif (plain == 1):
                    sliced.append((self.rubiks[i][x][y]))
                else:
                    sliced.append((self.rubiks[x][i][y]))

        #Only works with 3x3x3
        if reverse:
            sliced[0].swapQueue(sliced[6])
            sliced[1].swapQueue(sliced[3])
            sliced[2].swapQueue(sliced[0])
            sliced[3].swapQueue(sliced[7])
            sliced[5].swapQueue(sliced[1])
            sliced[6].swapQueue(sliced[8])
            sliced[7].swapQueue(sliced[5])
            sliced[8].swapQueue(sliced[2])
        else:
            sliced[0].swapQueue(sliced[2])
            sliced[1].swapQueue(sliced[5])
            sliced[2].swapQueue(sliced[8])
            sliced[3].swapQueue(sliced[1])
            sliced[5].swapQueue(sliced[7])
            sliced[6].swapQueue(sliced[0])
            sliced[7].swapQueue(sliced[3])
            sliced[8].swapQueue(sliced[6])

        for x in range(len(sliced)):
            sliced[x].swapCommitQueue()
            sliced[x].rotateCube(plain, reverse)
    
    def shuffle(self, n: int):
        for x in range(n):
            self.rotateRubiks(random.randint(0,self.size-1),random.randint(0,2), True if random.randint(0,1) == 1 else False)

    def getMoveLog(self):
        return self.logMoves

    def test(self):
        w = ""
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    w += "[{},{},{}]".format(x,y,z)
                w += "\t"
            w += "\n"
        print(w)