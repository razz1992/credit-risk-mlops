# Model Card — Credit Default Classifier

## Model details
- Name/version/training commit: TBD
- Type: Binary classifier; Logistic Regression baseline and tree candidate
- Framework: scikit-learn
- Status: Not yet trained

## Intended use
Educational demonstration of tabular supervised learning and the ML lifecycle.

## Out-of-scope use
Do not use for real lending, credit eligibility, pricing, collections, or consequential decisions about individuals.

## Data
UCI Default of Credit Card Clients dataset (ID 350). Consult the official record for provenance, feature definitions, and CC BY 4.0 terms.

## Evaluation
Populate from held-out test data. Report precision, recall, F1, ROC-AUC, PR-AUC, confusion matrix, class support, and selected threshold.

## Limitations and risks
- Historical data may not represent current lending conditions or populations.
- Demographic variables may be sensitive or act as proxies.
- Overall metrics can conceal group-level disparities.
- Probability scores are not causal explanations.
- Performance can degrade under data drift and population shift.
- No production governance or compliance approval exists.

## Future monitoring plan
Before real deployment, define input schema/distribution checks, monitor drift, track delayed ground-truth performance, version datasets/models, and define retraining and rollback criteria.
