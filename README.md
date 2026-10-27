# Machine Learning Portfolio

A collection of machine-learning case studies spanning classification, regression, recommendation systems, clustering and text analysis. The projects demonstrate the core workflow from defining a prediction task and preparing features to model training, evaluation and application integration.

**Core stack:** Python · Pandas · NumPy · scikit-learn · XGBoost · Flask · Streamlit

## Selected projects

| Project | Task | Methods represented |
|---|---|---|
| [Customer Churn Prediction](Customer_churn_Predict/) | Predict customer churn and serve predictions through a web app | Preprocessing pipeline, categorical encoding, scaling, XGBoost, Flask |
| [Breast Cancer Classification](Breast_Cancer/) | Classify malignant vs benign cases in a benchmark dataset | StandardScaler, Logistic Regression, GridSearchCV, Flask |
| [Crop Yield Prediction](Crop_Yeild_project/) | Predict yield from environmental and crop-related features | ColumnTransformer, OneHotEncoder, Decision Tree Regression, RMSE/R² |
| [Movie Recommendation System](Movie-Recommender_system/) | Recommend similar movies from metadata | Content-based filtering, cosine similarity, Streamlit |
| [Laptop Price Prediction](Laptop-Price-Predection-Regression-Project/) | Estimate price from device specifications | Feature engineering, preprocessing pipeline, XGBoost regression |

## Model development workflow

1. Define the target variable and intended use of predictions.
2. Inspect feature types, target balance, missing values, duplicates and leakage risks.
3. Prepare features and split data appropriately.
4. Build preprocessing and model steps into a reproducible workflow.
5. Establish a baseline and select task-appropriate evaluation metrics.
6. Tune model parameters and compare candidate models.
7. Evaluate model behavior and interpret important errors.
8. Connect the model to an inference workflow where the project includes an application.

## Skills demonstrated

- Classification and regression
- Feature engineering and preprocessing pipelines
- Model selection and hyperparameter tuning
- Evaluation with task-appropriate metrics
- Content-based recommendation and similarity analysis
- Flask/Streamlit application integration

## How to explore the portfolio

Open each project folder to review its problem statement, preprocessing workflow, model approach, evaluation and available application files. The focus is on understanding not only the selected model, but also how the prediction task is framed and how model outputs can support a decision.
