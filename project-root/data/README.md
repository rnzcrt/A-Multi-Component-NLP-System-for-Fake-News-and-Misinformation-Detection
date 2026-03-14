# Data

## LIAR Dataset
- **Source:** https://www.cs.ucsb.edu/~william/data/liar_dataset.zip
- **License:** Publicly available for NLP research
- **PII:** None — all statements are public political speech from PolitiFact.com
- **Splits:** Pre-defined train.tsv / valid.tsv / test.tsv (~10k / 1.3k / 1.3k)
- **Classes:** pants-fire, false, barely-true, half-true, mostly-true, true

## How to Obtain
```bash
python get_data.py
```
Raw files will be saved to `data/raw/`. Do NOT commit raw data to the repo.
```

---

### `requirements.txt`
```
torch>=2.0.0
transformers>=4.38.0
datasets>=2.18.0
scikit-learn>=1.4.0
spacy>=3.7.0
numpy>=1.26.0
pandas>=2.2.0
matplotlib>=3.8.0
seaborn>=0.13.0
tqdm>=4.66.0