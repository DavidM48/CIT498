import Helper

class Square:
    side = ""
    color = ""

    def __init__(self):
        pass

    def __init__(self, side, color):
        self.setSide(side)
        self.setColor(color)

    def setSide(self, side):
        if type(side) is int:
            self.side =  Helper.helper.sideDictRev[side]
        else:
            self.side = side

    def setColor(self, color):
        if type(color) is int:
            self.color = Helper.helper.colorDictRev[color]
        else:
            self.color = color

    def getSide(self):
        return self.side
    
    def getColor(self):
        return self.color
    
    def __str__(self):
        return "[Side: {} Color: {}]".format(self.side, self.color) 