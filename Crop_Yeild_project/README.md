# Crop Yield Prediction — Machine Learning + Flask

## Objective
Predict crop yield using historical environmental and crop-specific features such as rainfall, temperature, pesticide usage, area, year, and crop type.

## Workflow
**Data preparation → categorical encoding → feature preprocessing → regression → evaluation → Flask deployment**

## Model
- Decision Tree Regressor
- ColumnTransformer
- OneHotEncoder
- RMSE and R² evaluation
- Saved preprocessing and model artifacts

## Deployment
The Flask application accepts crop/environment inputs and returns predicted yield.

## Tech Stack
**Python | Pandas | NumPy | Scikit-learn | Decision Tree Regression | ColumnTransformer | Flask**

## Business Questions & Value
**Question:** How do the supplied weather, pesticide, area, year and crop features relate to predicted crop yield?

**Finding to communicate:** The saved Decision Tree Regressor and preprocessing artifacts generate a yield estimate. Report RMSE/R² from the notebook's held-out evaluation and state the target units and dataset scope before describing model quality.

**Business use and limitation:** The model can demonstrate how an agricultural planning workflow might estimate yield, but predictions should not be used for real planting or financial decisions without local validation and uncertainty analysis.

## Report / PDF
Review the notebook and available app screenshots in `static/`; a project PDF export was not identified in the folder listing.
