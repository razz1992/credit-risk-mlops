# Lesson 2 — Data Profiling and EDA Summary

## Dataset and schema

- **Dataset:** UCI Default of Credit Card Clients, dataset ID 350.
- **Rows:** 30,000.
- **Predictor columns:** 23.
- **Target:** `Y`, binary default-payment outcome.
- **Metadata:** UCI variable metadata identifies the source ID field separately from the 23 predictors. The ID is not included in `X` and must not be used as a model feature.
- **Missing values:** 0 in the inspected combined DataFrame.
- **Dtypes:** all 24 combined columns were reported as int64. Integer storage does not imply that every variable is continuous numeric.

## Feature groups used for EDA

| Group | Columns | Count |
|---|---|---:|
| Categorical | X2, X3, X4 | 3 |
| Repayment status (ordinal codes) | X6–X11 | 6 |
| Numerical | X1, X5, X12–X23 | 14 |
| Target | Y | 1 |

Semantic mapping: X1=credit limit; X2=sex; X3=education; X4=marital status; X5=age; X6–X11=monthly repayment status; X12–X17=bill statement amounts; X18–X23=previous payment amounts. Refer to the UCI documentation for full descriptions and historical month mapping.

## Categorical and repayment value checks

- X2 observed values: 1, 2; no unexpected values against the expected set {1, 2}.
- X3 observed values: 0, 1, 2, 3, 4, 5, 6. Values 0, 5, 6 fall outside the simple expected set {1, 2, 3, 4}; observed counts: 14, 280, 51 respectively.
- X4 observed values: 0, 1, 2, 3. Value 0 falls outside the simple expected set {1, 2, 3}; observed count: 54.
- X6–X11 include repayment codes from -2 through 8, with some categories absent in individual months. Preserve and interpret these codes using the dataset documentation; do not assume they are continuous measurements.

No recoding or removal was performed during EDA.

## Duplicate investigation

Three distinct duplicate measures were reported:

| Measure | Count |
|---|---:|
| Exact duplicate row occurrences across all 24 columns | 35 |
| Rows participating in those full-row duplicate groups | 70 |
| Duplicate feature occurrences when comparing X only | 56 |
| Repeated feature groups (grouped by all 23 predictors) | 52 |
| Repeated groups with one target value | 31 |
| Repeated groups with more than one target value | 21 |
| Rows belonging to conflicting-target groups | 46 |

The 21 conflicting groups contain identical predictor combinations with different target labels. This is a genuine ambiguity in the available feature representation. Do not deduplicate, relabel, or remove these records without a documented strategy and a leakage-safe split design. Consider keeping all records for the baseline, reporting this limitation, and performing a carefully designed sensitivity analysis later.

## Numerical distribution and IQR screening

All 14 numerical features had 30,000 non-null observations.

| Feature | IQR outlier count | Percentage |
|---|---:|---:|
| X1 | 167 | 0.5567% |
| X5 | 272 | 0.9067% |
| X12 | 2,400 | 8.0000% |
| X13 | 2,395 | 7.9833% |
| X14 | 2,469 | 8.2300% |
| X15 | 2,622 | 8.7400% |
| X16 | 2,725 | 9.0833% |
| X17 | 2,693 | 8.9767% |
| X18 | 2,745 | 9.1500% |
| X19 | 2,714 | 9.0467% |
| X20 | 2,598 | 8.6600% |
| X21 | 2,994 | 9.9800% |
| X22 | 2,945 | 9.8167% |
| X23 | 2,958 | 9.8600% |

IQR flags are statistical observations, not proof of invalid records. No outliers were removed or capped. Bill statement variables include negative observed minima; investigate their meaning rather than assuming invalidity. Payment variables have zero minima, which may be meaningful.

Selected descriptive statistics:
- X1: mean 167,484.32; median 140,000; range 10,000–1,000,000.
- X5: mean 35.49; median 34; range 21–79.
- Bill statement means (X12–X17) range from 38,871.76 to 51,223.33.
- Previous payment means (X18–X23) range from 4,799.39 to 5,921.16.

## Default-rate analysis

### By age group

| Age group | Count | Default rate |
|---|---:|---:|
| 21–30 | 11,013 | 22.4371% |
| 31–40 | 10,713 | 20.4331% |
| 41–50 | 6,005 | 23.2973% |
| 51–60 | 1,997 | 25.2379% |
| 61–79 | 272 | 26.8382% |

The 31–40 group has the lowest observed rate and the 61–79 group the highest, but the oldest group has only 272 records. These are descriptive associations, not causal effects.

### By X6 repayment status

| X6 code | Customers | Defaults | Default rate |
|---:|---:|---:|---:|
| -2 | 2,759 | 365 | 13.2294% |
| -1 | 5,686 | 954 | 16.7781% |
| 0 | 14,737 | 1,888 | 12.8113% |
| 1 | 3,688 | 1,252 | 33.9479% |
| 2 | 2,667 | 1,844 | 69.1414% |
| 3 | 322 | 244 | 75.7764% |
| 4 | 76 | 52 | 68.4211% |
| 5 | 26 | 13 | 50.0000% |
| 6 | 11 | 6 | 54.5455% |
| 7 | 9 | 7 | 77.7778% |
| 8 | 19 | 11 | 57.8947% |

Higher delinquency codes generally have higher observed default rates, especially codes 1–3. Estimates for codes 4–8 are based on small samples and are unstable. These are descriptive relationships, not causal effects.

## Pearson correlation with target Y

| Feature | Correlation |
|---|---:|
| X5 | 0.013890 |
| X17 | -0.005372 |
| X16 | -0.006760 |
| X15 | -0.010156 |
| X14 | -0.014076 |
| X13 | -0.014193 |
| X12 | -0.019644 |
| X23 | -0.053183 |
| X22 | -0.055124 |
| X20 | -0.056250 |
| X21 | -0.056827 |
| X19 | -0.058579 |
| X18 | -0.072929 |
| X1 | -0.153520 |

The heatmap shows strong positive intercorrelations among X12–X17 (bill statement amounts). This may create multicollinearity concerns for linear models. Pearson correlations with Y are mostly weak in magnitude; this does not establish that the features lack predictive value. Repayment-status codes are ordinal and were not included in this numerical-only target correlation table. Use model-based validation and appropriate metrics for feature assessment.

## EDA conclusions and provisional decisions

1. No missing-value imputation is indicated by the inspected data.
2. Investigate X3 codes 0, 5, 6 and X4 code 0; do not silently discard them.
3. Preserve repayment codes as categorical/ordinal information; choose encoding deliberately.
4. Do not remove IQR outliers automatically.
5. Do not deduplicate or relabel the 21 conflicting feature groups at this stage.
6. Use stratified splitting and fit all preprocessing only on training data.
7. Compare scaled Logistic Regression with tree-based models; evaluate class-sensitive metrics, not accuracy alone.
8. Keep the test set untouched during preprocessing and model selection.

## Scope and limitations

This document records the learner-shared Kaggle outputs. It does not claim causal relationships, final feature importance, a selected cleaning strategy, or trained-model performance. This is an educational project and not suitable for real credit decisions.
