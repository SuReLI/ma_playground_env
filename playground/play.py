import gym
import numpy as np
import pygame
import pygame.locals as pl
import time
import sys

sys.path.append('../')
ENV_NAME = 'PlaygroundNavigationHuman-v1'

from playground.reward_function import sample_descriptions_from_state, get_reward_from_state
from playground.descriptions import generate_all_descriptions
from playground.env_params import get_env_params
"""
Playing script. Control the agent with the arrows, close the gripper with the space bar.
"""

env = gym.make(ENV_NAME, reward_screen=False, viz_data_collection=True)
pygame.init()

env_params = get_env_params()
train_descriptions, test_descriptions, extra_descriptions = generate_all_descriptions(env_params)
all_descriptions = train_descriptions +  test_descriptions

# Select the goal to generate the scene.
goal_str = np.random.choice(all_descriptions)

env.reset()
env.unwrapped.reset_with_goal(goal_str)

key_maps = [
    [pl.K_DOWN, pl.K_UP, pl.K_LEFT, pl.K_RIGHT, pl.K_SPACE],
]

stop = False
while not stop:
    # init_render

    action = np.zeros([env_params["nb_agents"], 3])
    for event in pygame.event.get():
        if event.type == pl.KEYDOWN:
            for a in range(env_params["nb_agents"]):
                if event.key == key_maps[a][0]:
                    action[a, 1] = -1
                elif event.key == key_maps[a][1]:
                    action[a, 1] = 1
                elif event.key == key_maps[a][2]:
                    action[a, 0] = -1
                elif event.key == key_maps[a][3]:
                    action[a, 0] = 1
                elif event.key == key_maps[a][4]:
                    action[a, 2] = 1

            if event.key == pl.K_q:
                stop = True
            if action.sum() != 0:
                time.sleep(0.05)
                break

    out = env.step(action)
    env.render()

    # Sample descriptions of the current state
    train_descr, test_descr, extra_descr = sample_descriptions_from_state(out[0], env.unwrapped.params)
    descr = train_descr + test_descr
    print(descr)

    # assert that the reward function works, should give positive rewards for descriptions sampled, negative for others.
    for d in descr:
        assert get_reward_from_state(out[0], d, env_params)
    for d in np.random.choice(list(set(all_descriptions) - set(descr)), size=20):
        assert not get_reward_from_state(out[0], d, env_params)


