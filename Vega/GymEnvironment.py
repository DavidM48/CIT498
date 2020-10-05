import gym 
from gym import spaces
from gym.utils import seeding
import numpy

import Rubiks_Cube

class CustomEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, size=3): 

        self.lastMove = {}
        self.lastReward = 0
        self.done = False

        self.stepCount = 0   

        self.size = size
        self.rubiks = Rubiks_Cube.Rubiks(self.size)  

        self.action_space = spaces.Discrete(18)    
        self.observation_space = spaces.Discrete(20000)
        #self.observation_space = spaces.Discrete(43252003274489856000)

        #self.seed()
        self.reset()

    
    def encode(self):
        rubikscube = self.rubiks.getRubiks()
        counter = 0
        state = 0
        
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    if rubikscube[x][y][z].getID() > counter:
                        state += rubikscube[x][y][z].getID() * counter
                    elif (rubikscube[x][y][z].getID() == 0 and counter == 0):
                        state += 1
                    else:
                        state += rubikscube[x][y][z].getID() / counter
                    counter += 1
                        
                    
                    
        return int(state)

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action)
        if (action == 0):
            self.rubiks.rotateRubiks(0, 0, False)
        elif (action == 1):
            self.rubiks.rotateRubiks(0, 0, True)
        elif (action == 2):
            self.rubiks.rotateRubiks(1, 0, False)
        elif (action == 3):
            self.rubiks.rotateRubiks(1, 0, True)
        elif (action == 4):
            self.rubiks.rotateRubiks(2, 0, False)
        elif (action == 5):
            self.rubiks.rotateRubiks(2, 0, True)
        elif (action == 6):
            self.rubiks.rotateRubiks(0, 1, False)
        elif (action == 7):
            self.rubiks.rotateRubiks(0, 1, True)
        elif (action == 8):
            self.rubiks.rotateRubiks(1, 1, False)
        elif (action == 9):
            self.rubiks.rotateRubiks(1, 1, True)
        elif (action == 10):
            self.rubiks.rotateRubiks(2, 1, False)
        elif (action == 11):
            self.rubiks.rotateRubiks(2, 1, True)
        elif (action == 12):
            self.rubiks.rotateRubiks(0, 2, False)
        elif (action == 13):
            self.rubiks.rotateRubiks(0, 2, True)
        elif (action == 14):
            self.rubiks.rotateRubiks(1, 2, False)
        elif (action == 15):
            self.rubiks.rotateRubiks(1, 2, True)
        elif (action == 16):
            self.rubiks.rotateRubiks(2, 2, False)
        else:
            self.rubiks.rotateRubiks(2, 2, True)

        self.stepCount += 1

        test = self.rubiks.getLastMove()
        self.rubiks.rotateRubiks(test["i"], test["plain"], not test["reverse"])

        rb = self.rubiks.getRubiks()
        counter = 0
        score = 0

        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    if (rb[x][y][z].getID() == counter):
                        score += 1
                    counter += 1 

        reward = (score / (self.size**3))

        done = (reward == 1)
        
        self.lastMove = self.rubiks.getLastMove()
        self.lastReward = reward
        self.done = done

        return self.encode(), reward, done, {}
    
    def getRubiksCube(self):
        return self.rubiks


    def reset(self):
        if (self.rubiks.getShuffled()):
            self.rubiks.clearMoveLog()
            self.rubiks.creatFromLog(self.rubiks.getShuffleMoveLog())
        else:
            self.rubiks.shuffle(20)

        self.lastMove = {}
        self.lastReward = 0
        self.done = False

        self.stepCount = 0 
        return self.encode()

    def render(self, mode='human', close=False):
        print("Last Move: {}".format(self.lastMove))
        print("Last reward: {}".format(self.lastReward))
        print("done: {}".format(self.done))
        print("state:".format(self.encode()))

    def getStepCount(self):
        return self.stepCount
