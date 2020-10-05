import Rubiks_Cube
import Helper
import jsonHelper

import json
import copy
import time

import cProfile

#import GymEnvironment as RubiksEnv

#print(int(round(time.time() * 1000)))

#env = RubiksEnv.CustomEnv()
#print(env.encode())
#env.reset()
#print(env.encode())
#env.reset()
#print(env.encode())
#env.step(0)
#print(env.encode())

#cProfile.run('Rubiks_Cube.Rubiks(3)')

#rc.rotateRubiks(0,0,True)
#rc.shuffle(50)
#cProfile.run('rc.shuffle(20000)')
#t = copy.deepcopy(rc.getMoveLog())
#for x in range(len(t)):
    #rc.rotateRubiks(t[len(t) - 1 - x]["i"],t[len(t) - 1 - x]["plain"], False if t[len(t) - 1 - x]["reverse"] else True)

#f = open("moves.json", "w")
#json.dump(rc.getMoveLog(),f)
#f.close()

#jh = jsonHelper.JSONRubiksWrite(rc)

#f = open("test.json", "w")
#json.dump(jh.convertToJSON(), f)
#f.close()
current_milli_time = lambda: int(round(time.time() * 1000))
rc = Rubiks_Cube.Rubiks(3)
rc.shuffle(20000)
jh = jsonHelper.JSONRubiksWrite(rc)
f = open("{}.json".format(current_milli_time()), "w")
json.dump(jh.convertToJSON(), f)
f.close()
