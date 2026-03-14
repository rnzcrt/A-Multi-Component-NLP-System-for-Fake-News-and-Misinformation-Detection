# A Multi-Component NLP System for Fake News and Misinformation Detection

**6INTELSY Final Project — AY 2025-2026, 2nd Semester**
Holy Angel University — School of Computing

---

## Team

| Role | Member |
|------|--------|
| Project Lead / Integration | TBD |
| Data & Ethics Lead | TBD |
| Modeling Lead | TBD |
| Evaluation & MLOps Lead | TBD |

**Members:** Rian S. Cortez, Ryence S. Cortez, Ranz Emmanuel G. Cuarto, Mark Darius D. David, Charles Orville Pascua

---

## Project Overview

This system is an NLP-based misinformation detection pipeline combining:

- **Core Model:** Fine-tuned DistilBERT for veracity classification
- **CNN Component:** Text-CNN (Kim, 2014) as baseline and ablation
- **NLP Component:** NER-based provenance tagging (spaCy)
- **RL Component:** Contextual bandit for adaptive threshold tuning

---

## Dataset

[LIAR Dataset](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip) — 12,836 labeled political statements from PolitiFact.

---

## Quick Start

```bash
# 1. Setup environment
pip install -r requirements.txt

# 2. Download data
python data/get_data.py

# 3. Run full pipeline (train + eval, ~60 min on Colab T4)
bash run.sh
```

---

## Results (to be updated)

| Model | Macro-F1 | Accuracy |
|-------|----------|----------|
| Majority baseline | — | — |
| TF-IDF + Logistic Regression | — | — |
| Text-CNN | — | — |
| DistilBERT (fine-tuned) | — | — |

---

## Repo Structure

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
```

---

## Release Tags

| Tag | Description |
|-----|-------------|
| `v0.1` | Proposal & repo setup |
| `v0.9` | Release candidate |
| `v1.0` | Final submission |
