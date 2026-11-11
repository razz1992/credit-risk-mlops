import pandas as pd
import pytest

from credit_risk.data import TARGET_COLUMN, validate_dataset


def test_valid_dataset_schema() -> None:
    validate_dataset(pd.DataFrame({"feature": [1, 2], TARGET_COLUMN: [0, 1]}))


def test_missing_target_fails() -> None:
    with pytest.raises(ValueError, match="Missing target"):
        validate_dataset(pd.DataFrame({"feature": [1, 2]}))


def test_non_binary_target_fails() -> None:
    with pytest.raises(ValueError, match="binary"):
        validate_dataset(pd.DataFrame({"feature": [1], TARGET_COLUMN: [2]}))
