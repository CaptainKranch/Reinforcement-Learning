import gym #if you do not have gym, do pip install gym
import numpy as np
import time
import matplotlib.pyplot as plt

env = gym.make('FrozenLake-v0')
states = env.observation_space.n
actions = env.action_space.n

Q = np.zeros((states, actions))

episodes = 1500
max_steps = 100
learning_rate = 0.81
gamma = 0.96
render = False
epsilon = 0.95
rewards = []

for episode in range(episodes):
    state = env.reset()
    for _ in range(max_steps):
        if render:
            env.render()
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])

        next_state, reward, done, _ = env.step(action)

        Q[state, action] = Q[state, action] + learning_rate * (reward + gamma * np.max(Q[next_state, :]) - Q[state, action])

        state = next_state

        if done:
            rewards.append(reward)
            epsilon -= 0.001
            break

# print(Q)
# print(f'Average reward: {sum(rewards)/len(rewards)}:')

def get_average(values):
    return sum(values)/len(values)

avg_rewards = []

for i in range(0, len(rewards), 100):
    avg_rewards.append(get_average(rewards[i:i+100]))


plt.plot(avg_rewards)
plt.ylabel('Average reward')
plt.xlabel('episode 100\'s')
plt.show()
