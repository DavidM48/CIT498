import Helper

class Square:
    side = ""
    color = ""

    def __init__(self):
        pass

    def __init__(self, side: int, color: int):
        self.setSide(side)
        self.setColor(color)

    def setSide(self, side: int):
        self.side = side

    def setColor(self, color: int):
        self.color = Helper.helper.colorDictHex[Helper.helper.colorDictRev[color]]

    def setColorHex(self, color: int):
        self.color = color
            
    def getSide(self):
        return self.side
    
    def getColor(self):
        return self.color
    
    def __str__(self):
        return "[Side: {}, Color: {}]".format(Helper.helper.sideDictRev[self.side], hex(self.color)) 