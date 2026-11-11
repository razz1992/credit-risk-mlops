# Credit Risk ML — Production-Style Learning Project

A hands-on supervised ML project to train, evaluate, package, and serve a credit-default classifier. Educational use only; not a real credit decision system.

## Project organization

- [Specifications and project plan](specifications/planning.md)
- [Kaggle training workflow](specifications/KAGGLE_WORKFLOW.md)
- [Portfolio evidence and case study](specifications/portfolio/README.md)

## Compute strategy

Model training will run in Kaggle Notebooks, not on the local Windows machine. The local machine is used for source-code development, Git/GitHub, API integration, lightweight tests, and portfolio documentation. This tabular dataset does not require a GPU; start with Kaggle CPU and use an accelerator only if a later experiment justifies it.

## Planned capabilities

- UCI dataset ingestion and validation
- Leakage-aware preprocessing and stratified splits
- Logistic Regression baseline and tree-based model comparison
- Validation threshold selection and held-out test evaluation
- Experiment tracking and model packaging
- FastAPI inference endpoint
- Tests, GitHub Actions CI, and portfolio evidence

## Dataset

UCI Default of Credit Card Clients (ID 350). See the [official record](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients), cite dataset authors, and follow CC BY 4.0 terms.

## License

Choose the project source license before public release. Dataset licensing and attribution are separate.
