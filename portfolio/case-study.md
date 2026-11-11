# Case Study: Credit Default Classification with an End-to-End ML Lifecycle

## Executive summary
**Problem:** Estimate probability of future credit-card payment default from historical account and payment features.  
**Approach:** Reproducible supervised-learning workflow with baseline comparison, evaluation, threshold analysis, packaging, and API serving.  
**Status:** Planned. Populate results only after the final experiment.

## Dataset and provenance
- Source: UCI Machine Learning Repository, Default of Credit Card Clients (ID 350).
- Cite dataset authors and official UCI record.
- Features include repayment status, bill statements, and previous payments.
- Historical benchmark; representativeness and fairness limitations apply.

## Technical approach
1. Validate raw data and target distribution.
2. Create stratified train, validation, and test partitions.
3. Fit transformations inside an sklearn Pipeline to avoid leakage.
4. Compare Logistic Regression and a tree-based estimator.
5. Tune on training folds; select threshold using validation data.
6. Evaluate once on held-out test data.
7. Package pipeline and serve predictions through FastAPI.

## Results
Populate only from actual experiments; never invent metrics.

| Metric | Baseline | Selected model |
|---|---:|---:|
| Precision | TBD | TBD |
| Recall | TBD | TBD |
| F1 | TBD | TBD |
| ROC-AUC | TBD | TBD |
| PR-AUC | TBD | TBD |

Threshold: TBD  
Test-set size: TBD  
Experiment / commit: TBD

## Engineering and MLOps
Reproducible dependencies and seed; experiment metadata; model serialization; API schema validation; automated tests and CI.

## Decisions and trade-offs
Complete after comparing actual metrics, runtime, model complexity, and threshold-dependent errors.

## Limitations and responsible use
Educational project only. Not suitable for real credit decisions. Historical data may encode demographic and institutional biases. Group analysis and domain/legal review would be required before any consequential use. Probabilities are not causal explanations.

## What I learned
Complete as implementation progresses.
