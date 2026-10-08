# Breast Cancer Classification — Machine Learning + Flask

## Objective
Build a binary classification model to distinguish malignant and benign tumors and expose the trained model through a Flask application.

## Workflow
**Data preparation → feature scaling → model tuning → model persistence → Flask deployment**

## Modeling
- Target: tumor diagnosis
- Feature scaling with StandardScaler
- Logistic Regression
- GridSearchCV for hyperparameter tuning
- Saved trained model for inference

## Deployment
The Flask application accepts tumor-related inputs and returns a prediction through a simple web interface.

## Tech Stack
**Python | Pandas | Scikit-learn | Logistic Regression | GridSearchCV | StandardScaler | Flask**