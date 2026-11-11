# Lesson 3 — Preprocessing and Split Summary

## Dataset partitioning

| Partition | Rows | Features | Y=0 | Y=1 | Y=1 percentage |
|---|---:|---:|---:|---:|---:|
| Training | 19,208 | 23 | 14,945 | 4,263 | 22.19% |
| Validation | 4,796 | 23 | 3,739 | 1,057 | 22.04% |
| Test | 5,996 | 23 | 4,680 | 1,316 | 21.95% |
| Total | 30,000 | 23 | 23,364 | 6,636 | 22.12% |

The split is exactly 64% / 16% / 20%. Class proportions are closely preserved across partitions.

## Duplicate-aware grouping

- Unique feature groups: 29,944.
- Repeated feature occurrences: 56.
- Group identifiers were generated from all 23 predictors; target Y was excluded.
- The learner confirmed no identical feature groups cross partitions; leakage assertions passed.
- Conflicting labels remain in the dataset and are not removed or relabeled.

## Preprocessing

| Feature group | Columns | Transformation |
|---|---|---|
| Numerical | X1, X5, X12–X23 | Median imputation, then StandardScaler |
| Categorical and repayment status | X2–X4, X6–X11 | Most-frequent imputation, then OneHotEncoder(handle_unknown=ignore) |

A ColumnTransformer combines these branches. It was fitted only on X_train and used with transform() on validation and test data.

## Transformed dimensions

| Partition | Transformed shape |
|---|---:|
| Training | (19,208, 90) |
| Validation | (4,796, 90) |
| Test | (5,996, 90) |

The original 23 predictors expand to 90 transformed columns. The first 14 outputs are numerical features, followed by one-hot encoded categories including X2, X3, X4 and repayment-status codes.

## Scaling verification

The means of the 14 transformed numerical training columns were reported as approximately zero, consistent with StandardScaler fitted on training data.

## Methodological notes

1. The source ID is excluded from model inputs.
2. The target is kept separate from X.
3. Duplicate-aware splitting avoids identical feature vectors crossing partitions.
4. Conflicting labels remain a known dataset limitation.
5. Preprocessing is fitted only on training data to prevent leakage.
6. No model has been trained in this lesson; the test set has not been used for model selection or evaluation.

## Evidence note

This notebook is reconstructed from the code and outputs shared by the learner. Preserve the native Kaggle download alongside it if original Kaggle execution metadata is required.