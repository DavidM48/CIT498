import Rubiks_Cube
import Helper

#print(Helper.helper.sideDict)
rc = Rubiks_Cube.Rubiks(3)  
#rc.fillRubiks()
#rc.test()
#rc.rotateRubiks(0, True, False)
#pprint.pprint(rc.getRubiks())
print("Cube 1: ")
print(rc.getRubiks()[1][1][1])
print("Cube 2: ")
print(rc.getRubiks()[0][0][0])
rc.getRubiks()[1][1][1].swapQueue(rc.getRubiks()[0][0][0])
rc.getRubiks()[0][0][0].swapQueue(rc.getRubiks()[1][1][1])

rc.getRubiks()[1][1][1].swapCommitQueue()
rc.getRubiks()[0][0][0].swapCommitQueue()
print("Cube 1: ")
print(rc.getRubiks()[1][1][1])
print("Cube 2: ")
print(rc.getRubiks()[0][0][0])