import Cube
import Helper

import random

class Rubiks():
    
    def __init__(self, size = 3):
        if size < 3:
            raise ValueError("Size is too small use 3 or bigger.")
        self.size = size

        self.shuffled = False

        self.logMoves = {}
        self.logCount = 0

        self.logMovesShuffle = {}
        self.logCountShuffle = 0

        self.initRubiks()
        self.fillRubiks()
    
    def initRubiks(self):
        self.rubiks = [[[0 for col in range(self.size)] for col in range(self.size)] for row in range(self.size)] 

    def fillRubiks(self):
        top = (self.size - 2)
        id = 0
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    self.rubiks[x][y][z] = Cube.Cube(True, id)
                    self.rubiks[x][y][z].setCords(x, y, z)
                    if x <= top:
                        self.rubiks[x][y][z].removeSide(0)
                    if x >= 1:
                        self.rubiks[x][y][z].removeSide(1)
                    if y <= top:
                        self.rubiks[x][y][z].removeSide(2)
                    if y >= 1:
                        self.rubiks[x][y][z].removeSide(3)
                    if z <= top:
                        self.rubiks[x][y][z].removeSide(4)
                    if z >= 1:
                        self.rubiks[x][y][z].removeSide(5)
                    id += 1

    def getRubiks(self):
        return self.rubiks
    
    def getSize(self):
        return self.size

    def rotateRubiks(self, i: int, plain: int, reverse: bool, fromShuffle=False):
        if (plain > 2 or plain < 0):
            print("Warning \'plain\' is out of bounds {}".format(plain))
        if (i >= self.size or i < 0):
            raise ValueError("i is either to big or too small.")

        if (fromShuffle):
            self.logMovesShuffle[self.logCountShuffle] = {"i":i,"plain":plain,"reverse":reverse}
            self.logCountShuffle += 1
        else:
            self.logMoves[self.logCount] = {"i":i,"plain":plain,"reverse":reverse}
            self.logCount += 1

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
        if n <= 0:
            raise ValueError("N is too small: N needs to be 1 or bigger")
        self.clearShuffleMoveLog()
        for x in range(n):
            self.rotateRubiks(random.randint(0, self.size - 1),             # random number for i
                            random.randint(0, 2),                           # random number for plain
                            True if random.randint(0, 1) == 1 else False,   # random bool for reverse
                            True)
        self.shuffled = True   

    def getShuffled(self):
        return self.shuffled

    def creatFromLog(self, log):
        self.initRubiks()
        self.fillRubiks()
        for x in range(len(log)):
            self.rotateRubiks(log[x]["i"], log[x]["plain"], log[x]["reverse"])

    def clearMoveLog(self):
        self.logMoves = {}
        self.logCount = 0

    def clearShuffleMoveLog(self):
        self.shuffled = False 
        self.logMovesShuffle = {}
        self.logCountShuffle = 0

    def getMoveLog(self):
        return self.logMoves

    def getLastMove(self):
        return self.logMoves[len(self.logMoves)-1]

    def getShuffleMoveLog(self):
        return self.logMovesShuffle

    def test(self):
        w = ""
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    w += "[{},{},{}]".format(x,y,z)
                w += "\t"
            w += "\n"
        print(w)