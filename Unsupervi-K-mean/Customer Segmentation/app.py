import streamlit as st
import pandas as pd
import pickle

# Load trained scaler and K-Means
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('kmeans.pkl', 'rb') as f:
    kmeans = pickle.load(f)

with open('train_features.pkl', 'rb') as f:
    features = pickle.load(f)

st.title("Customer Segmentation Predictor")
st.write("Enter customer details to predict cluster")

#Take user input

# Numeric input
age = st.number_input("Age", min_value=18, max_value=100, value=30)
work_exp = st.number_input("Work Experience", min_value=0, max_value=50, value=5)
family_size = st.number_input("Family Size", min_value=1, max_value=10, value=3)

# Categorical input
gender = st.selectbox("Gender", ["Male", "Female"])
ever_married = st.selectbox("Ever Married", ["Yes", "No"])
graduated = st.selectbox("Graduated", ["Yes", "No"])
profession = st.selectbox("Profession", ["Engineer", "Lawyer", "Healthcare", "Entertainment"])
spending_score = st.selectbox("Spending Score", ["Low", "Average", "High"])
var_1 = st.selectbox("Var_1", ["Cat_1","Cat_2","Cat_3","Cat_4","Cat_5","Cat_6"])

#Convert input to DataFrame + One-Hot Encode

input_dict = {
    'Age': [age],
    'Work_Experience': [work_exp],
    'Family_Size': [family_size],
    'Gender': [gender],
    'Ever_Married': [ever_married],
    'Graduated': [graduated],
    'Profession': [profession],
    'Spending_Score': [spending_score],
    'Var_1': [var_1]
}

input_df = pd.DataFrame(input_dict)

# Categorical columns
cat_cols = ['Gender', 'Ever_Married', 'Graduated', 'Profession', 'Spending_Score', 'Var_1']

# One-hot encode
input_encoded = pd.get_dummies(input_df)

# Align columns with train features
input_encoded = input_encoded.reindex(columns=features, fill_value=0)


#Scale input + Predict Cluster

# Scale
input_scaled = scaler.transform(input_encoded)

# Predict cluster
cluster = kmeans.predict(input_scaled)

st.success(f"The predicted cluster for this customer is: {cluster[0]}")
