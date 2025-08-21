import streamlit as st
import pandas as pd
import pickle

# ---------------------------
# Load saved model (pipeline with preprocessing + ExtraTreesClassifier)
# ---------------------------
with open("final_extratrees_model.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------------------
# App title and styling
# ---------------------------
st.set_page_config(page_title="CKD Prediction App", page_icon="🩺", layout="wide")

st.markdown(
    """
    <style>
    .main { background-color: #f5f7fa; }
    .stButton>button {
        background-color: #4CAF50;
        color:white;
        font-size:16px;
        border-radius:10px;
        padding: 0.6em 1em;
    }
    .stButton>button:hover { background-color: #45a049; }
    .prediction-box {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🩺 Chronic Kidney Disease Prediction")
st.write("Fill in the patient details below and check if the patient may have CKD.")

# ---------------------------
# Sidebar Information
# ---------------------------
st.sidebar.header("ℹ️ About")
st.sidebar.write("""
This app uses a **Machine Learning model (Extra Trees Classifier)** trained on a CKD dataset.  
It analyzes patient medical parameters and predicts whether the patient has **Chronic Kidney Disease (CKD)**.
""")
st.sidebar.markdown("**Created by:** Rituraj")

# ---------------------------
# Input Form
# ---------------------------
with st.form("input_form"):
    st.subheader("🔍 Enter Patient Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", 1, 120, 45)
        blood_pressure = st.number_input("Blood Pressure (mmHg)", 50, 200, 80)
        specific_gravity = st.selectbox("Specific Gravity", [1.005, 1.010, 1.015, 1.020, 1.025])
        albumin = st.slider("Albumin", 0, 5, 1)
        sugar = st.slider("Sugar", 0, 5, 0)
        red_blood_cells = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
        pus_cell = st.selectbox("Pus Cell", ["normal", "abnormal"])

    with col2:
        pus_cell_clumps = st.selectbox("Pus Cell Clumps", ["present", "notpresent"])
        bacteria = st.selectbox("Bacteria", ["present", "notpresent"])
        blood_glucose_random = st.number_input("Blood Glucose Random (mg/dl)", 50, 500, 121)
        blood_urea = st.number_input("Blood Urea (mg/dl)", 1, 400, 36)
        serum_creatinine = st.number_input("Serum Creatinine (mg/dl)", 0.1, 20.0, 1.2)
        sodium = st.number_input("Sodium (mEq/L)", 100, 160, 138)
        potassium = st.number_input("Potassium (mEq/L)", 2.0, 8.0, 4.5)

    with col3:
        haemoglobin = st.number_input("Haemoglobin (g/dl)", 3.0, 20.0, 15.2)
        packed_cell_volume = st.number_input("Packed Cell Volume", 20, 60, 44)
        white_blood_cell_count = st.number_input("WBC Count (cells/cumm)", 2000, 25000, 7800)
        red_blood_cell_count = st.number_input("RBC Count (millions/cmm)", 2.0, 8.0, 5.2)
        hypertension = st.selectbox("Hypertension", ["yes", "no"])
        diabetes_mellitus = st.selectbox("Diabetes Mellitus", ["yes", "no"])
        coronary_artery_disease = st.selectbox("Coronary Artery Disease", ["yes", "no"])
        appetite = st.selectbox("Appetite", ["good", "poor"])
        peda_edema = st.selectbox("Pedal Edema", ["yes", "no"])
        aanemia = st.selectbox("Anaemia", ["yes", "no"])

    submitted = st.form_submit_button("🔎 Predict")

# ---------------------------
# Prediction
# ---------------------------
if submitted:
    # Prepare input data
    new_data = pd.DataFrame({
        'age': [age],
        'blood_pressure': [blood_pressure],
        'specific_gravity': [specific_gravity],
        'albumin': [albumin],
        'sugar': [sugar],
        'red_blood_cells': [red_blood_cells],
        'pus_cell': [pus_cell],
        'pus_cell_clumps': [pus_cell_clumps],
        'bacteria': [bacteria],
        'blood_glucose_random': [blood_glucose_random],
        'blood_urea': [blood_urea],
        'serum_creatinine': [serum_creatinine],
        'sodium': [sodium],
        'potassium': [potassium],
        'haemoglobin': [haemoglobin],
        'packed_cell_volume': [packed_cell_volume],
        'white_blood_cell_count': [white_blood_cell_count],
        'red_blood_cell_count': [red_blood_cell_count],
        'hypertension': [hypertension],
        'diabetes_mellitus': [diabetes_mellitus],
        'coronary_artery_disease': [coronary_artery_disease],
        'appetite': [appetite],
        'peda_edema': [peda_edema],
        'aanemia': [aanemia]
    })

    # Prediction
    prediction = model.predict(new_data)[0]

    if prediction == 0:
        st.markdown(
            '<div class="prediction-box" style="background-color:#ffcccc; color:#b30000;">⚠️ Patient HAS Chronic Kidney Disease</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="prediction-box" style="background-color:#ccffcc; color:#006600;">✅ Patient does NOT have Chronic Kidney Disease</div>',
            unsafe_allow_html=True
        )
