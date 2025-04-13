# Lab 13 Reinforcement Learning Lab Report

## Custom Reward Function 1 – Distance and Angle Penalty

**Reward Function Code Snippet:**
```python
reward = shaping - 100 * np.sqrt(np.square(state[0]) + np.square(state[1])) - 100 * abs(state[4])
```

**Explanation:**
This reward function penalizes the lander for both horizontal/vertical displacement from the landing pad (`state[0]`, `state[1]`) and deviation from vertical orientation (`state[4]`, the angle). The closer and more upright the lander is, the higher the reward.

**Intended Effect:**
The idea was to strongly encourage the agent to descend vertically over the landing pad, ideally promoting a more direct and controlled descent.

**Training Result:**
- **Average Reward**: **-176.74**

**Analysis:**
Although the agent attempted to hover close to the pad, the heavy penalties likely discouraged meaningful exploration. The agent became overly cautious and prioritized staying upright rather than descending effectively, which hurt long-term rewards.

---

## Custom Reward Function 2 – Leg Contact Bonus

**Reward Function Code Snippet:**
```python
reward = shaping + 10 * (legs[0] and legs[1])
```

**Explanation:**
This function adds a **+10 reward** if **both legs make contact** with the ground simultaneously, encouraging stable and balanced landings. The base shaping reward remains unchanged.

**Intended Effect:**
Rewarding balanced leg contact should reinforce good landing technique while avoiding erratic movements that lead to crashes or single-leg landings.

**Training Result:**
- **Average Reward**: **-99.63**

**Analysis:**
This reward significantly improved performance. The bonus encouraged the agent to aim for soft and balanced landings, aligning well with the environment's objectives.

---

## Custom Reward Function 3 – High Velocity Penalty

**Reward Function Code Snippet:**
```python
reward = shaping - 10 * np.sqrt(np.square(state[2]) + np.square(state[3]))
```

**Explanation:**
This reward penalizes the lander for having high horizontal and vertical velocities (`state[2]`, `state[3]`). Lower speeds are rewarded, encouraging the agent to make slower, more controlled movements.

**Intended Effect:**
To encourage soft and slow landings by discouraging excessive speed, which often leads to crashing or bouncing.

**Training Result:**
- **Average Reward**: **-143.38**

**Analysis:**
This function helped reduce crash frequency, but the agent often hesitated or hovered too long, possibly due to fear of penalty from descent speed. While safer, the behavior lacked decisiveness needed to maximize rewards.

---

## Conclusion
Each reward function shaped the agent's learning in unique ways:
- **Reward Function 1** focused on position and angle but discouraged exploration.
- **Reward Function 2** showed the best result by promoting balanced landings.
- **Reward Function 3** reduced crashes but made the agent overly cautious.

Overall, Reward Function 2 struck the best balance between guidance and freedom, resulting in the highest average reward.

