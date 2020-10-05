import numpy as np
import random
import time
import json

import jsonHelper

import GymEnvironment as RubiksEnv

env = RubiksEnv.CustomEnv()

alpha = 0.1
gamma = 0.6
epsilon = 0.9

q_table = np.zeros([env.observation_space.n, env.action_space.n])

current_milli_time = lambda: int(round(time.time() * 1000))

for i in range(1, 5):
    state = env.reset()
    epochs, penalties, reward, = 0, 0, 0
    done = False
    while not done and env.getStepCount() < 1000:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample() # Explore action space
        else:
            action = np.argmax(q_table[state]) # Exploit learned values
        #action = env.action_space.sample() # Explore action space
        next_state, reward, done, info = env.step(action) 
        
        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])
        
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] = new_value

        if reward == -10:
            penalties += 1

        state = next_state
        epochs += 1
        print("state: {}, step: {}, reward: {}".format(state, action, new_value))
        #env.render()
    #save log file here
    jh = jsonHelper.JSONRubiksWrite(env.getRubiksCube())
    f = open("{}.json".format(current_milli_time()), "w")
    json.dump(jh.convertToJSON(), f)
    f.close()

print("Training finished.")