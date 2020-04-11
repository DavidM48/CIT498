    #  Mine   -- Three
    #0 west   -- south
    #1 south  -- north
    #2 north  -- top
    #3 east   -- bottom
    #4 top    -- west
    #5 bottom -- east
class helper:
    sideDict = {"South":0,"North":1,"Top":2,"Bottom":3,"West":4,"East":5}
    sideDictRev = {0:"South", 1:"North", 2:"Top", 3:"Bottom", 4:"West", 5:"East"}

    colorDict = {"White":0,"Red":1,"Green":2,"Blue":3,"Orange":4,"Yellow":5, "Empty":6}
    colorDictRev = {0:"White", 1:"Red", 2:"Green", 3:"Blue", 4:"Orange", 5:"Yellow", 6:"Empty"}
    
    colorDictHex = {"White":0xffffff,"Red":0xff0000,"Green":0x00ff00,"Blue":0x0000ff,"Orange":0xffae00,"Yellow":0xffff00, "Empty":0x000000}
    colorDictHexNum = {0:0xffffff, 1:0xff0000, 2:0x00ff00, 3:0x0000ff, 4:0xffae00, 5:0xffff00, 0:0x000000}