import gym
env = gym.make("CartPole-v0")
for i_episode in range(20):
    observation = env.reset()
    for _ in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        print(action)
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(i_episode+1))
            break
env.close()