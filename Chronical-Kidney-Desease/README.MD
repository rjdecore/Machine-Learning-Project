# Chronic Kidney Disease Prediction — Machine Learning

## Objective
Build an end-to-end classification pipeline to predict whether a patient is likely to have chronic kidney disease.

## Workflow
**EDA → cleaning/standardization → preprocessing → model comparison → pipeline → Streamlit deployment**

## Models Compared
The project evaluates multiple classifiers including:
- KNN
- Decision Tree
- Random Forest
- Extra Trees
- XGBoost
- CatBoost
- LightGBM

The documented analysis selects **Extra Trees Classifier** as the best-performing model.

## Deployment
A Streamlit application accepts input parameters and returns the model prediction using the saved preprocessing/model pipeline.

## Tech Stack
**Python | Pandas | NumPy | Scikit-learn | XGBoost | CatBoost | LightGBM | Streamlit**