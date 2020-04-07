import Rubiks_Cube
import Cube
import Square
import Helper

import json


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