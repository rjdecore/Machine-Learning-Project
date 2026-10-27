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

## Business Questions & Value
**Question:** What price does the model estimate for a laptop given its brand, CPU/GPU, RAM, storage, display and other specifications?

**Finding to communicate:** The Streamlit app uses a saved preprocessing/model pipeline to return an estimated price. Quote RMSE/R² only from the notebook's held-out evaluation and explain the currency, target transformation and error scale.

**Business use:** The project demonstrates a specification-based price-estimation workflow that could support comparison or listing-price research; it is not a guarantee of current market price.

## Report / PDF
[Open the code PDF](code%20pdf.pdf), notebook and Streamlit app.
