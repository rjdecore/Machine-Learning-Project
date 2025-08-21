# 🩺 Chronic Kidney Disease (CKD) Prediction  

This project predicts whether a person is likely to have **Chronic Kidney Disease (CKD)** or not, using **Machine Learning models** and an **interactive Streamlit web app**.  

---

## 📌 Project Overview  
- Performed **EDA (Exploratory Data Analysis)** to understand trends in the CKD dataset.  
- **Cleaned and standardized** data (renamed columns, replaced categorical values, handled missing values).  
- Trained multiple ML models (**KNN, Decision Tree, Random Forest, Extra Trees, XGBoost, CatBoost, LightGBM, etc.**) and compared accuracies.  
- **Extra Trees Classifier** performed the best.  
- Built an **end-to-end ML pipeline** (preprocessing + model).  
- Deployed an **interactive Streamlit app** where users can input health parameters and get predictions.  

---

## 📊 Dataset  
- **Source**: Chronic Kidney Disease dataset (UCI ML Repository)  
- **Target column**: `class` →  
  - `0` → Has CKD  
  - `1` → Does not have CKD  

---

## ⚙️ Tech Stack  
- 🐍 **Python 3**  
- 📊 **Pandas, Numpy** → Data handling  
- 📈 **Matplotlib, Seaborn** → Visualization  
- 🤖 **Scikit-learn, XGBoost, CatBoost, LightGBM** → Model training  
- 🌐 **Streamlit** → Web app  

---

## 🚀 Features  
✅ Cleaned and processed CKD dataset  
✅ Trained and tuned multiple ML models  
✅ Selected **Extra Trees Classifier** as final model  
✅ Built **ML pipeline** (no need for manual preprocessing at prediction time)  
✅ Streamlit app with **interactive design**  
✅ Prediction output:  
   - **"Has Chronic Kidney Disease"**  
   - **"Does Not Have Chronic Kidney Disease"**  

---

## 📂 Repository Structure  



📂 Repository Structure
CKD-Prediction/
│
├── ckd_notebook.ipynb      # Jupyter Notebook with EDA + model training
├── app.py                  # Streamlit app
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── model.pkl               # Saved ML pipeline (Extra Trees Classifier)

#▶️ How to Run
1. Clone the repository
https://github.com/rjdecore/Machine-Learning-Project/edit/main/Chronical-Kidney-Desease.git
cd CKD-Prediction
