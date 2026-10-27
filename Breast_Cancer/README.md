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

## Business Questions & Value
**Question:** Can the supplied diagnostic features distinguish the dataset's malignant and benign cases?

**Finding to communicate:** The model returns a binary prediction from the saved preprocessing/model artifacts. Report precision, recall, confusion matrix and the test-set setup from the notebook before discussing performance; accuracy alone can hide missed malignant cases.

**Business use and limitation:** This is a learning/demo project, not a clinical diagnostic tool. Real clinical use requires rigorous external validation and qualified medical oversight.

## Report / PDF
[Open the code PDF](notebook%20and%20dataset/code_pdf.pdf), the notebook and the Flask app.
