# Machine Learning Portfolio

A collection of machine-learning projects spanning classification, regression, recommendation systems, clustering and text analysis. Projects vary in scope and implementation maturity; consult each project's files and README for the workflow actually implemented.

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

1. Define the prediction target and how the model will be used.
2. Inspect target balance, feature types, missing values, leakage risks and duplicates.
3. Split data appropriately before fitting transformations.
4. Build preprocessing and modeling steps into a reproducible pipeline where possible.
5. Establish a baseline and choose metrics appropriate to the task.
6. Tune hyperparameters using cross-validation on training data only.
7. Evaluate once on held-out data and explain errors, limitations and likely deployment drift.
8. Persist the fitted preprocessing/model pipeline and validate inference on unseen examples.

## Evaluation standards

- **Classification:** report appropriate metrics such as precision, recall, F1, ROC-AUC and a confusion matrix; consider class imbalance and threshold choice.
- **Regression:** report metrics such as MAE/RMSE and R², compare against a simple baseline and inspect residuals.
- **Recommendation:** explain the similarity method, candidate-generation limits and how recommendation quality would be evaluated.
- **Deployment:** verify that training and inference use identical feature names, order and preprocessing.

## Quality notes

The README descriptions indicate methods associated with each project, but do not by themselves prove model quality or generalization. Before quoting performance numbers, verify the notebook, split strategy, leakage controls, validation results and saved pipeline. Avoid making clinical or other high-stakes claims from a demo model.

Each project folder contains its own implementation and available supporting files.
