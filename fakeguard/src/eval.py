"""
eval.py — Evaluation entry point for FakeGuard.
Reports: Accuracy, Macro-F1, Confusion Matrix, Calibration (ECE).
Usage: python src/eval.py --config experiments/configs/default.yaml
"""

import argparse
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="experiments/configs/default.yaml")
    args = parser.parse_args()

    with open(args.config) as f:
        cfg = yaml.safe_load(f)

    print(f"[eval.py] Config: {cfg}")
    print("[eval.py] Evaluation stub — to be implemented in Week 2.")


if __name__ == "__main__":
    main()
