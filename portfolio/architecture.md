# Architecture

## Training lifecycle
```mermaid
flowchart TD
  A[UCI public dataset] --> B[Ingestion]
  B --> C[Schema and quality validation]
  C --> D[Stratified train / validation / test split]
  D --> E[Preprocessing Pipeline]
  E --> F[Baseline and candidate training]
  F --> G[Cross-validation and tuning]
  G --> H[Validation threshold selection]
  H --> I[Held-out test evaluation]
  I --> J[Model artifact + metrics + metadata]
```

## Inference lifecycle
```mermaid
flowchart TD
  A[Client request] --> B[FastAPI schema validation]
  B --> C[Loaded preprocessing + model pipeline]
  C --> D[Probability and class prediction]
  D --> E[JSON response]
```

## Production considerations
The local project demonstrates packaging, validation, testing, tracking, and serving. It does not implement production identity/access management, durable remote artifact storage, autoscaling, SLOs, drift alerting, or regulated model governance.
