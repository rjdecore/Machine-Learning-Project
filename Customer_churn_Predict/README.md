## 📊 Customer Churn Prediction with Flask Deployment
**🚀 Project Overview**

**Customer churn is a critical issue for businesses, especially in sectors like banking, telecom, and SaaS.
This project builds a Machine Learning model to predict whether a customer will churn or not, and deploys it as a Flask web application with a modern UI.**

# 🔹 ML Workflow

- Data Preprocessing (handling categorical & numerical features)

- Feature Scaling and Encoding using ColumnTransformer

- Model Training with XGBoost

- Saving pipeline with Pickle (preprocessor.pkl & xgboost_churn_model.pkl)

- Flask Web App for deployment

# 🖼️ Web App Preview
[!web_page][d.png](Customer_churn_Predict/static/web.png)

**✨ The web app allows users to input customer details and get a prediction with probability.**

## 📌 Form Input + Prediction Output

Input Form (Left)	Prediction Result (Right)

	
## ⚙️ Tech Stack

- Python 3.9+

- Flask – Web framework

- Scikit-learn – Preprocessing

- XGBoost – Model training

## Project Structure
Customer_Churn/
│
├── app.py                  # Flask application
├── requirements.txt        # Dependencies
│
├── Model/
│   ├── xgboost_churn_model.pkl   # Trained ML model
│   └── preprocessor.pkl          # ColumnTransformer (scaler+encoder)
│
├── templates/
│   └── index.html           # Web form UI
│
└── static/
    └── style.css            # CSS styling


HTML + CSS – Frontend UI


**Clone the Repository**
'''
git clone [https://github.com/yourusername/customer-churn-flask](https://github.com/rjdecore/Machine-Learning-Project/edit/main/Customer_churn_Predict).git
cd customer-churn-flask '''




Pickle – Model persistence
