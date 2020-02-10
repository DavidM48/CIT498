import Cube
import Helper

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

    def test(self):
        w = ""
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    w += "[{},{},{}]".format(x,y,z)
                w += "\t"
            w += "\n"
        print(w)

#print(Helper.helper.sideDict)
rc = Rubiks(3)  
#rc.fillRubiks()
#rc.test()
#pprint.pprint(rc.getRubiks())
#print(rc.getRubiks()[1][1][0])
print(rc.getRubiks()[0][0][0])