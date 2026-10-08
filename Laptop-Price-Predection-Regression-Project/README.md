# Laptop Price Prediction — XGBoost + Streamlit

## Objective
Predict laptop prices from configuration features such as brand, type, RAM, CPU, GPU, storage, screen, and operating system.

## Feature Engineering
- Extracted CPU/GPU brands
- Converted RAM and weight
- Encoded touchscreen/IPS
- Converted screen resolution into X/Y resolution features and PPI
- Simplified operating-system categories
- Split HDD and SSD storage
- Log-transformed price

## Modeling
- ColumnTransformer + Pipeline
- XGBoost Regressor
- Evaluation with R² and RMSE
- Saved trained pipeline

## Deployment
Interactive Streamlit UI accepts laptop specifications and returns a predicted price.

## Tech Stack
**Python | Pandas | NumPy | Scikit-learn | XGBoost | Feature Engineering | Streamlit**