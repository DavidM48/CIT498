import Cube
import Helper

import math
import pprint
import copy

class Rubiks():
    def __init__(self):
        pass

    def __init__(self, size):
        self.size = size
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
                    if y <= 1:
                        self.rubiks[x][y][z].removeSide(1)
                    if y >= 1:
                        self.rubiks[x][y][z].removeSide(2)
                    #remove east or west
                    if z <= 1:
                        self.rubiks[x][y][z].removeSide(3)
                    if z >= 1:
                        self.rubiks[x][y][z].removeSide(0)
                    #remove top or bottom
                    if x <= 1:
                        self.rubiks[x][y][z].removeSide(5)
                    if x >= 1:
                        self.rubiks[x][y][z].removeSide(4)

    def getRubiks(self):
        return self.rubiks

    #plain 
    # 0 = vertical = z
    # 1 = horizontal = x
    # 2 = = y
    def rotateRubiks(self, i: int, plain: int, reverse: bool):
        if (i >= self.size or i < 0):
            #Check to make sure i is within limits
            pass
        
        sliced = list()

        #Fill the list with the cubes we need to swap
        for x in range(self.size):
            for y in range(self.size):
                if (plain == 0):
                    sliced.append((self.rubiks[x][y][i]))
                elif (plain == 1):
                    sliced.append((self.rubiks[i][x][y]))
                else:
                    sliced.append((self.rubiks[x][i][y]))
        
        #temp - prints out list of seleted squares
        for x in range(len(sliced)):
            print("{}, {}".format(sliced[x].getCords(), sliced[x].getNumberOfSides()))

        #Pair up each cube then add them to a swap queue 
        #Then commit queue
        #Need to make sure the sides remain the same as the oringal, ex cube at 0,0,0 should not have a side on the bottom
        if reverse:
            for x in range(len(sliced) - 1, -1, -1):
                pass
        else:
            for x in range(len(sliced)):
                for y in range(x + 1, len(sliced)):
                    if sliced[x].getNumberOfSides() == sliced[y].getNumberOfSides() and not sliced[y].queueState():
                        sliced[y].swapQueue(sliced[x])
                        break
            #might need to fix this for cubes bigger than 3x3
            sliced[0].swapQueue(sliced[len(sliced) - 1])
            sliced[1].swapQueue(sliced[len(sliced) - 2])
        
        for x in range(len(sliced)):
            #print(sliced[x].queueState())
            sliced[x].swapCommitQueue()
            #sliced[x].rotateCube(plain, reverse)
        
    def test(self):
        w = ""
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    w += "[{},{},{}]".format(x,y,z)
                w += "\t"
            w += "\n"
        print(w)