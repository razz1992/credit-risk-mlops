# Kaggle Training Workflow

## Decision

Use Kaggle Notebooks as the training environment. The local Windows machine is for editing, Git operations, API integration, tests that do not require heavy training, and packaging portfolio material.

## Why Kaggle

- Provides hosted notebook compute and a managed Python environment.
- Keeps training workloads away from the local machine.
- Supports versioned notebook runs and downloadable outputs.
- GPU acceleration is available where enabled, but this tabular credit-default dataset does not require a GPU. Start with CPU; use an accelerator only if a later experiment benefits from it.

## Working convention

1. Keep canonical source code in this Git repository under `src/credit_risk/`.
2. Create a Kaggle Notebook for each substantial training milestone, with the notebook source saved/exported into `specifications/portfolio/step-outputs/`.
3. At the end of every lesson, download the notebook (`.ipynb`) and relevant outputs from Kaggle.
4. Put evidence in the matching numbered step folder: notebook, concise Markdown notes, JSON metrics, and plots where relevant.
5. Never upload API keys, credentials, private data, or Kaggle secrets to Git.
6. Do not commit the raw dataset or large model binaries by default. Store reproducible instructions and metrics; use Kaggle output/model versioning or Git LFS only if explicitly needed.
7. Keep a small `run_metadata.json` for each training run: dataset version/source, notebook version, Git commit, seed, package versions, model parameters, and timestamp.
8. After review, commit source changes and selected small portfolio evidence to GitHub.

## Kaggle Notebook naming convention

`credit-risk-mlops-<step>-<short-description>`

Example: `credit-risk-mlops-04-baseline-training`.

## Step output naming convention

- `01-environment/kaggle-environment.md`
- `02-data-profiling/data-profile.md`, `data-quality.json`
- `03-eda/eda-summary.md`, `figures/*.png`
- `04-training/baseline-training.ipynb`, `training-summary.md`
- `05-evaluation/evaluation-report.md`, `metrics.json`, `confusion-matrix.png`, `roc-curve.png`, `precision-recall-curve.png`
- `06-experiment-tracking/mlflow-run-summary.md`
- `07-api-and-tests/api-test-report.md`, sanitized screenshots

## Important reproducibility rules

- Set and record a fixed random seed.
- Record the exact dataset version and source citation.
- Keep the test set untouched until model selection and threshold selection are complete.
- Fit preprocessing only on training data, inside the sklearn Pipeline.
- Do not report validation metrics as test metrics.
- Record all model comparisons, including the baseline.
- Portfolio claims must be supported by actual notebook outputs.

## Compute and cost control

Use Kaggle's free hosted compute subject to the account's current quotas and availability. Do not assume a specific GPU model or uninterrupted session. Save notebook checkpoints and outputs regularly. Avoid unnecessary GPU use for this small tabular dataset.
