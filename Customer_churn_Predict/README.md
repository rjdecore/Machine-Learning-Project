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