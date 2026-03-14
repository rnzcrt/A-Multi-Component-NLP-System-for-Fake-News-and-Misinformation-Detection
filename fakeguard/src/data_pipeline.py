"""
data_pipeline.py — Preprocessing and dataset loading for FakeGuard.
Handles LIAR dataset loading, label collapsing, tokenization, and splits.
Usage: python src/data_pipeline.py
"""

import os
import pandas as pd

RAW_DIR = os.path.join("data", "raw")

LABEL_MAP = {
    "pants-fire": 0, "false": 0, "barely-true": 0,
    "half-true":  1, "mostly-true": 1, "true": 1,
}

COLUMNS = [
    "id", "label", "statement", "subject", "speaker",
    "job_title", "state", "party", "barely_true_count",
    "false_count", "half_true_count", "mostly_true_count",
    "pants_fire_count", "context",
]


def load_split(split="train"):
    path = os.path.join(RAW_DIR, f"{split}.tsv")
    df = pd.read_csv(path, sep="\t", header=None, names=COLUMNS)
    df["binary_label"] = df["label"].map(LABEL_MAP)
    df = df.dropna(subset=["binary_label", "statement"])
    df["binary_label"] = df["binary_label"].astype(int)
    return df[["statement", "binary_label", "party", "speaker"]]


def get_datasets():
    train = load_split("train")
    val   = load_split("valid")
    test  = load_split("test")
    print(f"Train: {len(train)} | Val: {len(val)} | Test: {len(test)}")
    return train, val, test


if __name__ == "__main__":
    train, val, test = get_datasets()
    print(train["binary_label"].value_counts())
