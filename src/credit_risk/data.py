"""Dataset ingestion and validation utilities."""
from __future__ import annotations

import pandas as pd
from ucimlrepo import fetch_ucirepo

TARGET_COLUMN = "default_payment_next_month"


def load_dataset() -> pd.DataFrame:
    """Fetch UCI dataset 350 and return one frame with a normalized target name."""
    dataset = fetch_ucirepo(id=350)
    features = dataset.data.features.copy()
    targets = dataset.data.targets.copy()
    if targets.shape[1] != 1:
        raise ValueError(f"Expected one target column, got {list(targets.columns)}")
    target = targets.iloc[:, 0].rename(TARGET_COLUMN)
    return pd.concat([features, target], axis=1)


def validate_dataset(frame: pd.DataFrame) -> None:
    """Fail fast when required target/schema assumptions are not met."""
    if frame.empty:
        raise ValueError("Dataset is empty")
    if TARGET_COLUMN not in frame.columns:
        raise ValueError(f"Missing target column: {TARGET_COLUMN}")
    if frame[TARGET_COLUMN].isna().any():
        raise ValueError("Target contains missing values")
    labels = set(frame[TARGET_COLUMN].unique().tolist())
    if not labels.issubset({0, 1}):
        raise ValueError(f"Target must be binary 0/1; found {labels}")
