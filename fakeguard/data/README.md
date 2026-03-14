# Data

## LIAR Dataset

- **Source:** https://www.cs.ucsb.edu/~william/data/liar_dataset.zip
- **License:** Publicly available for NLP research
- **PII:** None — all statements are public political speech from PolitiFact.com
- **Splits:** Pre-defined train.tsv / valid.tsv / test.tsv (~10k / 1.3k / 1.3k)
- **Classes:** pants-fire, false, barely-true, half-true, mostly-true, true

## How to Obtain

```bash
python data/get_data.py
```

Raw files will be saved to `data/raw/`. Do NOT commit raw data to the repo.
