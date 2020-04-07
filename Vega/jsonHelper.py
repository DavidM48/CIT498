import Rubiks_Cube
import Cube
import Square
import Helper

import json

## This Clas converts the data that we need to work with 
# into a dictionary to then be converted into a json file

class JSONRubiksWrite():

    def __init__(self, rubiks: Rubiks_Cube.Rubiks):
        self.rubiks = rubiks.getRubiks()
        self.size = rubiks.getSize()
    
    def getCube(self, cube: Cube.Cube):
        return {"sides":cube.getNumberOfSides(),"colors":cube.getColorArray()}
    
    def convertToJSON(self):
        result = {}
        for x in range(self.size):
            result[x] = {}
            for y in range(self.size):
                result[x][y] = {}
                for z in range(self.size):
                    result[x][y][z] = self.getCube(self.rubiks[x][y][z])
        return result  