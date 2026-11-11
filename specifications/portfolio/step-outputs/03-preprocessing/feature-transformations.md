# Feature Transformation Design — Lesson 3

## Feature groups

- Numerical (14): X1, X5, X12, X13, X14, X15, X16, X17, X18, X19, X20, X21, X22, X23.
- Nominal categorical (3): X2, X3, X4.
- Repayment status (6): X6, X7, X8, X9, X10, X11.

## Numerical branch

1. SimpleImputer(strategy=median)
2. StandardScaler()

The median and scaling statistics are learned from training rows only.

## Categorical and repayment branch

1. SimpleImputer(strategy=most_frequent)
2. OneHotEncoder(handle_unknown=ignore)

One-hot encoding avoids imposing equal numeric distances between nominal category codes or repayment-status codes. Unknown categories at inference are ignored rather than raising an error.

## Combined transformer

ColumnTransformer routes the 14 numerical features through the numerical branch and the remaining 9 categorical/repayment features through the categorical branch. Remainder is dropped so only explicitly selected columns enter the model.

## Observed output

- Original predictor count: 23.
- Transformed feature count: 90.
- Training matrix: (19208, 90).
- Validation matrix: (4796, 90).
- Test matrix: (5996, 90).
- Training numerical means: approximately zero.

## Leakage control

Call fit_transform only on X_train. Call transform on X_val and X_test. Never fit preprocessing on the full dataset or independently fit it on validation/test data.

## Next step

In Lesson 4, place this preprocessor and the classifier in one sklearn Pipeline so the same fitted transformations are applied during training, serialization and inference.