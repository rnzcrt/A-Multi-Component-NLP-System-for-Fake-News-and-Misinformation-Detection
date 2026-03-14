#!/bin/bash
# One-command reproduce
# Usage: bash run.sh
set -e

echo "=== Fake News Detection: Full Pipeline ==="

echo "[1/5] Installing dependencies..."
pip install -r requirements.txt --quiet
python -m spacy download en_core_web_sm --quiet

echo "[2/5] Downloading data..."
python data/get_data.py

echo "[3/5] Preprocessing..."
python src/data_pipeline.py

echo "[4/5] Training (Text-CNN + DistilBERT + RL agent)..."
python src/train.py --config experiments/configs/default.yaml

echo "[5/5] Evaluation..."
python src/eval.py --config experiments/configs/default.yaml

echo "=== Done! Results saved to experiments/results/ ==="
