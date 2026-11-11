# Lesson 1 — Dataset Acquisition and Initial Profile

## Dataset provenance

- **Name:** Default of Credit Card Clients
- **Repository:** UCI Machine Learning Repository
- **Dataset ID:** 350
- **Official page:** https://archive.ics.uci.edu/dataset/350/default+credit+card+clients
- **Access method:** `ucimlrepo.fetch_ucirepo(id=350)`
- **Target column returned by the client:** `Y`

## Shape

| Object | Rows | Columns |
|---|---:|---:|
| Features (`X`) | 30,000 | 23 |
| Target (`y`) | 30,000 | 1 |
| Combined DataFrame | 30,000 | 24 |

The combined DataFrame used columns `X1` through `X23`, plus `Y`.

## Initial schema and quality checks

- All 24 columns were reported as `int64`.
- All 30,000 rows had non-null values in every column.
- Missing values: **0**.
- Exact duplicate rows reported by `df.duplicated().sum()`: **35**.
- Duplicate-row rate relative to all rows: approximately **0.117%**.
- Reported DataFrame memory usage: approximately **5.5 MB**.

**Duplicate handling decision:** No rows were removed in Lesson 1. Investigate the duplicate records and decide on a defensible handling strategy during data profiling, before train/test splitting. Do not assume that every repeated feature vector is erroneous without examining the records and target labels.

## Target distribution

| Target | Interpretation | Count | Percentage |
|---:|---|---:|---:|
| 0 | No default | 23,364 | 77.88% |
| 1 | Default | 6,636 | 22.12% |
| **Total** | | **30,000** | **100.00%** |

The positive/default class represents 22.12% of the observations. This is a class imbalance that must be considered when selecting evaluation metrics. Accuracy alone will not adequately describe model performance; include precision, recall, F1, ROC-AUC and PR-AUC in the evaluation plan.

## Data dictionary follow-up

The client returned generic feature labels `X1`–`X23`. Retrieve and document the official variable descriptions before interpreting individual columns or making feature-engineering decisions. Do not infer meanings from the numeric labels.

## Lesson 1 conclusion

Dataset acquisition and initial inspection succeeded. The observed shape matches the expected 30,000-row, 23-feature, one-target structure. No missing values were observed. Duplicate records and the official feature-name mapping remain explicit follow-up items for Lesson 2.
