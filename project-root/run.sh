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
```

---

### GitHub Issues (add these one by one to your Project Board)
```
Issue #1:  [Setup]    Initialize repo structure and README
Issue #2:  [Data]     Write get_data.py download script for LIAR dataset
Issue #3:  [Data]     Verify splits and class distribution (EDA stub)
Issue #4:  [Modeling] Scaffold src/data_pipeline.py with TSV loader
Issue #5:  [Modeling] Scaffold Text-CNN architecture in src/models/
Issue #6:  [Modeling] Scaffold DistilBERT fine-tune script in src/train.py
Issue #7:  [NLP]      Scaffold NER provenance module with spaCy
Issue #8:  [RL]       Define bandit environment spec and reward function
Issue #9:  [Ethics]   Draft initial ethics risk register (top 3 risks)
Issue #10: [Docs]     Write proposal PDF and tag v0.1 release
```

---

### Folder Structure to Create on GitHub
```
project-root/
  README.md
  LICENSE
  requirements.txt
  run.sh
  data/
    README.md
    get_data.py
  src/
    data_pipeline.py
    models/
    train.py
    eval.py
    rl_agent.py
    utils/
  notebooks/
    01_eda.ipynb
  experiments/
    configs/
    logs/
    results/
  docs/
    proposal.pdf