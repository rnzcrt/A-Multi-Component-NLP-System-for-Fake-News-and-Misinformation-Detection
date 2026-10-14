# A Multi-Component NLP System for Fake News and Misinformation Detection

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-DistilBERT_%C2%B7_Text--CNN_%C2%B7_spaCy-8A2BE2)
![Group Project](https://img.shields.io/badge/Type-Group_school_project-lightgrey)

**6INTELSY Final Project**, AY 2025–2026, 2nd Semester, Holy Angel University, School of Computing.

**Team:** Rian S. Cortez, Ryence S. Cortez, Ranz Emmanuel G. Cuarto, Mark Darius D. David, Charles Orville Pascua

## Project Overview

An NLP-based misinformation detection pipeline that combines:

- **Core model:** fine-tuned DistilBERT for veracity classification
- **CNN component:** Text-CNN (Kim, 2014) as a baseline and for ablation
- **NLP component:** NER-based provenance tagging (spaCy)
- **RL component:** a contextual bandit for adaptive threshold tuning

## Dataset

[LIAR dataset](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip): 12,836 labeled political statements from PolitiFact.

## Quick Start

```bash
# 1. Set up the environment
pip install -r requirements.txt

# 2. Download the data
python data/get_data.py

# 3. Run the full pipeline (train + evaluate, about 60 minutes on a Colab T4 GPU)
bash run.sh
```

## Repository Structure

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

## AI Credits

AI tools were used to help draft parts of this README.
