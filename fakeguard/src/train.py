"""
train.py — Training entry point for FakeGuard.
Supports: TF-IDF+LR baseline, Text-CNN, and fine-tuned DistilBERT.
Usage: python src/train.py --config experiments/configs/default.yaml
"""

import argparse
import random
import yaml
import numpy as np


def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch
        torch.manual_seed(seed)
    except ImportError:
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="experiments/configs/default.yaml")
    args = parser.parse_args()

    with open(args.config) as f:
        cfg = yaml.safe_load(f)

    set_seed(cfg.get("seed", 42))
    print(f"[train.py] Config: {cfg}")
    print("[train.py] Training stub — to be implemented in Week 2.")


if __name__ == "__main__":
    main()
