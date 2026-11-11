# Lesson 1 — Kaggle Environment

## Execution environment

| Item | Observed value |
|---|---|
| Notebook | `credit-risk-mlops-01-environment-setup` (as named in the lesson; verify actual Kaggle title) |
| Python | 3.13.18 |
| Platform | Linux x86_64, glibc 2.39 |
| Working directory | `/kaggle/working` |
| Accelerator | CPU (configured for this project) |
| NumPy | 2.1.3 |
| Pandas | 2.3.3 |
| Scikit-learn | 1.6.1 |
| Matplotlib | 3.10.0 |

## Verification

- Python and package imports executed successfully.
- Dataset retrieval through `ucimlrepo` completed.
- Kaggle displayed a package-restart advisory. No restart was required for the successful imports and operations reported in this run.

## Reproducibility follow-ups

- Record a fixed random seed in the notebook before any randomized split or model experiment.
- Record the Kaggle notebook version/run date and the Git commit used for the run.
- Download the executed `.ipynb` from Kaggle and preserve it in this folder. The notebook file was not included in the output shared for this documentation update.

## Scope

This environment is used for dataset exploration and model training. The local Windows repository remains the canonical source-code and Git workspace.
