# Customer Churn Prediction — XGBoost + Flask

## Business Objective
Predict whether a customer is likely to churn and expose the model through a simple web application.

## ML Workflow
**Data preprocessing → categorical encoding + numerical scaling → XGBoost training → pipeline persistence → Flask inference**

## Implementation
- ColumnTransformer for mixed data types
- Feature scaling
- Categorical encoding
- XGBoost classifier
- Saved preprocessor and trained model
- Prediction probability returned by the web app

## Deployment
Users enter customer attributes through the Flask UI and receive churn prediction with probability.

## Tech Stack
**Python | Pandas | Scikit-learn | ColumnTransformer | XGBoost | Flask | Model Persistence**

## Business Questions & Value
**Question:** Which customers are predicted to churn based on the available customer attributes, and what probability does the model assign?

**Finding to communicate:** The app returns a model prediction and probability. Add model performance numbers only after confirming held-out evaluation results, class balance and the selected probability threshold in the notebook.

**Business use:** Customer-success teams could use scores to prioritize retention outreach for review, but predictions should be evaluated for false positives, false negatives and fairness before operational use.

## Report / PDF
[Open the project code/report PDF](code.pdf), the notebook and the saved model/preprocessor artifacts.
