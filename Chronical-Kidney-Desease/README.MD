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

## Business Questions & Value
**Question:** Which input patterns does the trained classifier associate with the dataset's chronic-kidney-disease labels?

**Finding to communicate:** The README documents Extra Trees as the selected model after comparing several classifiers. Include test-set metrics and validation details only from the notebook's recorded results.

**Business use and limitation:** This is an educational ML demonstration, not a medical diagnostic or treatment recommendation. Clinical use would require external validation, clinical governance and expert oversight.

## Report / PDF
[Open the full Python-code PDF](Full_python_code.pdf), the notebook and the Streamlit app.
