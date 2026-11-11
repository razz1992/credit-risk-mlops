# Lesson 1 — Kaggle Environment

## Execution environment

| Item | Observed value |
|---|---|
| Platform | Kaggle Notebook, Linux x86_64, glibc 2.39 |
| Python | 3.13.18 |
| Working directory | `/kaggle/working` |
| Accelerator | **No Accelerator** — CPU runtime; confirmed by the supplied Kaggle session panel |
| NumPy | 2.1.3 |
| Pandas | 2.3.3 |
| Scikit-learn | 1.6.1 |
| Matplotlib | 3.10.0 |

## Kaggle resource panel snapshot

- Session elapsed at screenshot: 1 hour 2 minutes.
- Session limit displayed: 12 hours.
- Disk used: 2 GiB; displayed maximum: 57.6 GiB.
- CPU utilization at screenshot: 0.00%.
- RAM used at screenshot: approximately 759.4 MiB; displayed maximum: 30 GiB.

These are point-in-time values from the supplied screenshot, not performance benchmarks.

## Verification

- Python and package imports executed successfully.
- Dataset retrieval through `ucimlrepo` completed.
- Kaggle displayed a package-restart advisory. No restart was required for the successful imports and operations reported in this run.

## Notebook evidence

- `credit-risk-mlops-01-environment-setup.ipynb` contains the lesson code and the execution outputs shared by the learner.
- This notebook was reconstructed from the code/results shared in the conversation; it is not claimed to be a direct download of the original Kaggle notebook. Re-run it in Kaggle and download the native notebook if you want to preserve Kaggle's own execution metadata and cell outputs.

## Reproducibility follow-ups

- Record a fixed random seed before randomized splits and model experiments.
- Record the Kaggle notebook version/run timestamp and the Git commit used for the run.
- Preserve the official feature descriptions and dataset provenance.
- Do not remove duplicates until their structure and impact have been examined.

## Scope

Kaggle is used for dataset exploration and model training. The local Windows repository remains the canonical source-code and Git workspace.
