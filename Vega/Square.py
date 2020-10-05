import Helper

class Square:
    color = ""

    def __init__(self, color: int):
        self.position = color
        self.setColor(color)

    def setColor(self, color: int):
        self.color = Helper.helper.colorDictHexNum[color]
    
    def setPos(self, pos: int):
        self.position = pos

    def setColorOverride(self, color: int):
        self.color = color

    def setColorHex(self, color: int):
        #Might not be neeeded
        print(color) 
        self.color = color           
    
    def getColor(self):
        return self.color

    def getPos(self):
        return self.position
    
    def __str__(self):
        return "[Color: {}]".format(hex(self.color)) 