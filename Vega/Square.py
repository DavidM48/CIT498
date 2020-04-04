import Helper

class Square:
    color = ""

    def __init__(self):
        pass

    def __init__(self, color: int):
        self.setColor(color)

    def setColor(self, color: int):
        self.color = Helper.helper.colorDictHex[Helper.helper.colorDictRev[color]]

    def setColorHex(self, color: int):
        self.color = color           
    
    def getColor(self):
        return self.color
    
    def __str__(self):
        return "[Color: {}]".format(hex(self.color)) 