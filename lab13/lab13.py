from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
import gymnasium as gym
import numpy as np
import os

# === Reward Functions ===
def myreward1(state, original_reward):
    return 1 if state == 15 else 0

def myreward2(state, original_reward):
    if state == 15:
        return 1
    elif state in [5, 7, 11, 12]:
        return -1
    return 0

def myreward3(state, original_reward):
    return 1 if state == 15 else -0.05

# === Custom Reward Wrapper ===
class CustomRewardWrapper(gym.Wrapper):
    def __init__(self, env, reward_function):
        super(CustomRewardWrapper, self).__init__(env)
        self.reward_function = reward_function

    def step(self, action):
        state, reward, done, truncated, info = self.env.step(action)
        reward = self.reward_function(state, reward)
        return state, reward, done, truncated, info

# === Training Function ===
def train_agent(reward_fn, reward_name):
    print(f"Training with reward: {reward_name}")
    
    # Setup environment with custom reward
    env = gym.make('FrozenLake-v1', render_mode='rgb_array', desc=None, map_name="4x4", is_slippery=False)
    env = CustomRewardWrapper(env, reward_fn)

    log_path = f"./lab13/ppo_frozenlake_tensorboard/{reward_name}"
    model = PPO("MlpPolicy", env, verbose=1, tensorboard_log=log_path)

    # Train
    model.learn(total_timesteps=10000, progress_bar=True)

    # Save
    save_path = f"./lab13/ppo_frozenlake_{reward_name}"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    model.save(save_path)
    return model, env

# === Evaluation ===
def evaluate(model, env, reward_name):
    mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10)
    print(f"[{reward_name}] Mean reward: {mean_reward:.2f} +/- {std_reward:.2f}")

# === Run All Reward Functions ===
reward_configs = [
    (myreward1, "myreward1"),
    (myreward2, "myreward2"),
    (myreward3, "myreward3")
]

for reward_fn, name in reward_configs:
    model, env = train_agent(reward_fn, name)
    evaluate(model, env, name)
