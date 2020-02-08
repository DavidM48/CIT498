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
    
    def defaultCube(self):
        self.dc = Cube.Cube(True)

    def initRubiks(self):
        self.rubiks = [[[0 for col in range(self.size)] for col in range(self.size)] for row in range(self.size)] 

    def fillRubiks(self):
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    self.rubiks[x][y][z] = copy.deepcopy(self.dc)
    
    def getRubiks(self):
        return self.rubiks

#print(Helper.helper.sideDict)
rc = Rubiks(3)  
rc.fillRubiks()
#pprint.pprint(rc.getRubiks())
print(rc.getRubiks()[0][0][0])
#print(rc.getRubiks()[0][0][0])

#test = Cube.Cube()
#test.addSide("Top","Red")
#test.addSide("Bottom","White")
#test.addSide("Left","Green")
#test.addSide("Right","Blue")
#test.addSide("Front","Orange")
#test.addSide("Back","Yellow")
#print(test)