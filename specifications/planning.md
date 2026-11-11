# Production-Style Machine Learning Project — Planning

**Project:** Credit Default Risk Classifier  
**Status:** Bootstrap / planning  
**Target duration:** 1–2 focused days  
**Goal:** Learn the supervised ML lifecycle: train, evaluate, package, and serve a model locally.  
**Important:** Educational portfolio project only. It is not a credit-decision product.

## 1. Problem statement

Train a binary classifier to estimate whether a credit-card client will default on payment in the next period, using the UCI Default of Credit Card Clients dataset. Compare a baseline with a tree-based model, evaluate minority-class performance, select a threshold on validation data, persist the trained pipeline, and expose an inference API.

**Dataset:** UCI Machine Learning Repository, Default of Credit Card Clients (ID 350). Includes repayment status, bill statements, and payment history. Dataset file is approximately 5.3 MB, license CC BY 4.0. Cite the UCI record and original authors in all public reuse.

## 2. Learning outcomes

- Supervised learning, binary classification, features, target, leakage, and class imbalance.
- Stratified train / validation / test splits and held-out test discipline.
- Reproducible preprocessing with sklearn Pipeline and ColumnTransformer.
- Logistic Regression baseline vs. Random Forest or HistGradientBoosting candidate.
- Confusion matrix, precision, recall, F1, ROC-AUC, PR-AUC; why accuracy alone is inadequate.
- Threshold tuning based on an explicit error-cost trade-off.
- Reproducible training, config, experiment tracking, serialization, inference.
- Unit tests, API validation, CI, model/data limitations, portfolio communication.

## 3. Scope and non-goals

### MVP
1. Ingest public dataset and record provenance/license.
2. Validate schema, target, nulls, duplicates, and class distribution.
3. Stratified train/validation/test split with fixed seed.
4. Preprocessing + estimator as one sklearn Pipeline to avoid leakage.
5. Train Logistic Regression baseline and one stronger tree-based candidate.
6. Small bounded hyperparameter search using training data and cross-validation.
7. Select probability threshold on validation data; evaluate once on test data.
8. Save complete fitted pipeline and JSON metrics report.
9. FastAPI prediction endpoint with request schema and health endpoint.
10. Tests, lint/format, GitHub Actions CI, documentation, and portfolio evidence.

### Out of scope
Cloud deployment, Kubernetes, feature store, streaming, distributed training, deep learning/GPU, automated retraining, production monitoring infrastructure, and real lending decisions.

## 4. Proposed stack

| Area | Choice | Reason |
|---|---|---|
| Language | Python 3.11 | Stable package support |
| Data | pandas, NumPy, ucimlrepo | Tabular data |
| ML | scikit-learn | Pipeline, preprocessing, models, metrics, CV |
| API | FastAPI + Uvicorn | Local inference |
| Tracking | MLflow local file tracking (stretch) | Record params, metrics, artifacts |
| Testing | pytest, httpx | Unit and API tests |
| Quality | Ruff | Lint and formatting |
| Config | YAML | Reproducibility |
| Versioning | Git + GitHub | Source history |
| CI | GitHub Actions | Validate pushes and PRs |

Pin exact versions after verifying installation. Avoid introducing infrastructure that does not add learning value.

## 5. Two-day execution plan

### Day 1 — Data, training, evaluation
| Timebox | Task | Exit criteria |
|---|---|---|
| 30 min | Verify Python/Git, create venv | Environment works |
| 45 min | Dataset ingestion/schema | Data profile and target distribution |
| 45 min | EDA and data validation | Quality and leakage notes |
| 60 min | Split + preprocessing pipeline | Test data never used to fit transforms |
| 60 min | Baseline Logistic Regression | Baseline metrics saved |
| 60 min | Tree model + bounded tuning | Candidate chosen on validation |
| 45 min | Threshold analysis + final test | Confusion matrix and metrics |
| 30 min | Save model/metadata/plots | Reusable local artifact |

### Day 2 — Serving, tests, CI, portfolio
| Timebox | Task | Exit criteria |
|---|---|---|
| 45 min | Model loading + FastAPI | /health and /predict work |
| 45 min | Unit and API tests | pytest passes |
| 30 min | Input validation/error handling | Invalid requests rejected |
| 45 min | MLflow tracking (stretch) | Experiment run visible |
| 30 min | GitHub Actions CI | Workflow passes |
| 60 min | README, architecture, model card | Portfolio narrative complete |
| 30 min | Screenshots/demo | Sanitized evidence ready |
| 30 min | Final review and Git commits | Clean repository |

Finish MVP before stretch tasks. Schedule is a target, not a guarantee; package or environment issues may require trimming optional work.

## 6. ML lifecycle architecture

1. **Ingest:** UCI dataset -> local raw data (ignored by Git).
2. **Validate:** schema, target, nulls, duplicates, allowed categories.
3. **Split:** stratified train / validation / test with fixed random seed.
4. **Transform:** numeric scaling and categorical encoding as appropriate; fit only in training pipeline.
5. **Train:** Logistic Regression baseline and tree-based candidate.
6. **Tune:** bounded cross-validation search on training data.
7. **Select:** model and threshold using validation data and an explicit error-cost assumption.
8. **Evaluate:** final held-out test pass.
9. **Track:** code revision, params, metrics, dataset provenance, artifacts.
10. **Package:** serialize complete preprocessing + estimator pipeline and metadata.
11. **Serve:** FastAPI loads model once at startup and validates requests.
12. **Verify:** tests, CI, smoke test, and limitations documentation.

## 7. Evaluation strategy

- Report class counts and majority-class baseline.
- Report precision, recall, F1, ROC-AUC, PR-AUC, and confusion matrix.
- Use stratification.
- Select threshold on validation data, not test data.
- Evaluate the held-out test set only after model/threshold choices are fixed.
- State the intended operating point and false-positive / false-negative trade-off.
- Record random seed and package versions.

## 8. Responsible ML and risk controls

- The historical benchmark may not represent current applicants, geographies, or lending environments.
- Demographic variables may encode sensitive or proxy information. Keep the benchmark reproducible first, then document feature governance and sensitivity/fairness analysis as an extension.
- Do not claim fairness from a single metric. Group analyses require valid definitions, adequate sample sizes, and domain/legal review.
- No real customer data, secrets, credentials, or PII in Git.
- Do not commit raw data, model binaries, or MLflow run artifacts unless licensing and size have been reviewed.
- Predictions are model estimates, not causal explanations or financial recommendations.

## 9. Repository structure

```text
.
├── planning.md
├── README.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── .python-version
├── configs/config.yaml
├── data/raw/              # downloaded data; ignored
├── data/processed/        # generated data; ignored
├── models/                # model binaries; ignored
├── reports/               # selected reports/plots
├── mlruns/                # local MLflow; ignored
├── src/credit_risk/
│   ├── __init__.py
│   ├── data.py
│   ├── train.py
│   ├── evaluate.py
│   └── api.py
├── tests/
├── .github/workflows/ci.yml
└── portfolio/
    ├── README.md
    ├── case-study.md
    ├── model-card.md
    ├── architecture.md
    ├── assets/
    └── screenshots/
```

## 10. Portfolio deliverables

The `portfolio/` directory is separate from implementation:
- **README.md:** short public overview and links.
- **case-study.md:** problem, approach, experiments, actual results, decisions, limitations, lessons.
- **model-card.md:** intended use, out-of-scope use, data provenance, metrics, risks.
- **architecture.md:** lifecycle and serving diagram.
- **assets/:** architecture image, evaluation plots, sanitized output examples.
- **screenshots/:** tracking UI, API docs, tests/CI, and terminal demo.

Publish only actual measured metrics. No fabricated or placeholder results should be represented as completed work.

## 11. Git and release strategy

- Initialize Git locally; use meaningful conventional commits, e.g. `chore: bootstrap project structure`, `feat: implement data ingestion`.
- GitHub repository target: `razz1992/credit-risk-mlops`.
- Use `main` as default; feature branches for meaningful milestones if useful.
- CI runs lint and tests.
- Tag milestones only when complete, e.g. `v0.1.0-bootstrap`, then `v1.0.0`.
- Ignore `.env`, venv, caches, raw data, model binaries, and MLflow artifacts.
- Track code, configs, docs, tests, and small sanitized reports.

## 12. Definition of done

- [ ] Fresh environment installs dependencies.
- [ ] Dataset retrieved with attribution.
- [ ] Data validation and split reproducible.
- [ ] Baseline and candidate trained.
- [ ] Validation threshold documented.
- [ ] Final test metrics saved.
- [ ] Pipeline reloads and predicts.
- [ ] FastAPI health and prediction endpoints work.
- [ ] Tests and lint pass locally and in CI.
- [ ] README and portfolio case study honest and complete.
- [ ] No secrets, personal data, or generated artifacts accidentally committed.

## 13. Tutorial format

For every lesson: explain the production concept; inspect relevant code; let you implement key logic; review and correct; run on your machine; inspect actual results; then commit a small change. Do not advance until the current step works and its output is understood.

## 14. References

- UCI dataset: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients
- scikit-learn: https://scikit-learn.org/stable/
- MLflow tracking: https://mlflow.org/docs/latest/ml/tracking/
- FastAPI: https://fastapi.tiangolo.com/
- GitHub Actions: https://docs.github.com/actions


## 15. Compute environment and portfolio evidence workflow

Training will be performed in Kaggle Notebooks because the local machine is not the intended training host. Use the local machine for source edits, Git/GitHub, lightweight tests, API integration, and documentation. This dataset is small tabular data; Kaggle CPU is the default and a GPU is optional, not a requirement.

For every lesson, preserve the notebook source and relevant evidence under `specifications/portfolio/step-outputs/<step-number>-<step-name>/`. Include concise Markdown findings, JSON metrics, and plots where relevant. Keep actual outputs only; do not fabricate results. Do not commit raw datasets, secrets, or large model binaries by default. Follow [KAGGLE_WORKFLOW.md](KAGGLE_WORKFLOW.md) for naming, reproducibility, and export rules.
