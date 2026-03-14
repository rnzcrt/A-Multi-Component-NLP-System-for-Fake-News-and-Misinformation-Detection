"""
rl_agent.py — Contextual Bandit for adaptive threshold tuning.

Environment spec
----------------
State:   [macro_f1, false_positive_rate, false_negative_rate]  (floats in [0,1])
Actions: threshold values in {0.30, 0.35, 0.40, ..., 0.70}   (9 discrete actions)
Reward:  -(alpha * FPR + beta * FNR)
         alpha > beta — penalizes false positives more (flagging real news as fake
         has a higher social cost than missing a false claim in this setting).

Algorithm: epsilon-greedy bandit (Week 2 will extend to Q-learning if time allows).
"""

import numpy as np

THRESHOLDS = list(np.round(np.arange(0.30, 0.75, 0.05), 2))
ALPHA = 2.0  # false-positive penalty weight
BETA  = 1.0  # false-negative penalty weight


def reward(fpr: float, fnr: float) -> float:
    return -(ALPHA * fpr + BETA * fnr)


class ThresholdBandit:
    """Epsilon-greedy contextual bandit for decision-threshold selection."""

    def __init__(self, epsilon: float = 0.1, lr: float = 0.05):
        self.q       = {t: 0.0 for t in THRESHOLDS}
        self.epsilon = epsilon
        self.lr      = lr
        self.history = []   # (threshold, reward) log for learning curves

    def select(self) -> float:
        if np.random.rand() < self.epsilon:
            return float(np.random.choice(THRESHOLDS))
        return max(self.q, key=self.q.get)

    def update(self, threshold: float, r: float):
        self.q[threshold] += self.lr * (r - self.q[threshold])
        self.history.append((threshold, r))

    def best(self) -> float:
        return max(self.q, key=self.q.get)


if __name__ == "__main__":
    agent = ThresholdBandit()
    print("[rl_agent.py] ThresholdBandit initialized.")
    print(f"  Action space : {THRESHOLDS}")
    print(f"  Reward weights: alpha={ALPHA} (FP), beta={BETA} (FN)")
    print("[rl_agent.py] Full training loop to be wired in Week 2.")
