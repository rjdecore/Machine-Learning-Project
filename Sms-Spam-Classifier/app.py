import streamlit as st
import joblib
import re

# Load model and vectorizer (already uploaded to Colab)
vectorizer = joblib.load("vectorizer.joblib")
model = joblib.load("model.joblib")

# Function to clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Streamlit UI
st.title("SMS Spam Detection")
sms_input = st.text_area("Enter SMS:")

if st.button("Predict"):
    if sms_input:
        cleaned_sms = clean_text(sms_input)
        vectorized_sms = vectorizer.transform([cleaned_sms])
        prediction = model.predict(vectorized_sms)[0]
        if prediction == 1:
            st.error("🚨 This message is Spam!")
        else:
            st.success("✅ This message is Not Spam!")
    else:
        st.warning("Please enter an SMS message.")
