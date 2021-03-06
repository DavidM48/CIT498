import Rubiks_Cube
import Cube
import Square
import Helper

import json

## This Class converts the data that we need to work with 
# into a dictionary to then be converted into a json file

class JSONRubiksWrite():

    def __init__(self, rubiks: Rubiks_Cube.Rubiks):
        assert(rubiks != None)
        self.rubikscube = rubiks
        self.rubiks = rubiks.getRubiks()
        self.size = rubiks.getSize()
    
    def getCube(self, cube: Cube.Cube):
        return {"sides":cube.getNumberOfSides(),"colors":cube.getColorArray()}
    
    def convertToJSON(self):
        result = {"size":self.size}
        result["movesShuffle"] = self.convertMovesToJSON(True) 
        result["moves"] = self.convertMovesToJSON(False)
        for x in range(self.size):
            result[x] = {}
            for y in range(self.size):
                result[x][y] = {}
                for z in range(self.size):
                    result[x][y][z] = self.getCube(self.rubiks[x][y][z])
        return result  

    def convertMovesToJSON(self, shuffleLog=True):
        moves = self.rubikscube.getShuffleMoveLog() if shuffleLog else self.rubikscube.getMoveLog()
        result = {"steps":len(moves)}
        for x in range(len(moves)):
            result[x] = [moves[x]["i"], moves[x]["plain"], moves[x]["reverse"]]
        return result