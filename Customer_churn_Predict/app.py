from flask import Flask, request, render_template
import pickle
import pandas as pd
import os

# Initialize Flask
app = Flask(__name__)

# Get base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model and preprocessor (ColumnTransformer)
model = pickle.load(open(os.path.join(BASE_DIR, "Model/xgboost_churn_model.pkl"), "rb"))
preprocessor = pickle.load(open(os.path.join(BASE_DIR, "Model/preprocessor.pkl"), "rb"))

# ------------------- ROUTES -------------------

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect raw input values from form
        CreditScore = float(request.form['CreditScore'])
        Geography = request.form['Geography']
        Gender = request.form['Gender']
        Age = float(request.form['Age'])
        Tenure = int(request.form['Tenure'])
        Balance = float(request.form['Balance'])
        NumOfProducts = int(request.form['NumOfProducts'])
        HasCrCard = int(request.form['HasCrCard'])
        IsActiveMember = int(request.form['IsActiveMember'])
        EstimatedSalary = float(request.form['EstimatedSalary'])

        # Create DataFrame with same columns as training
        input_df = pd.DataFrame([{
            'CreditScore': CreditScore,
            'Geography': Geography,
            'Gender': Gender,
            'Age': Age,
            'Tenure': Tenure,
            'Balance': Balance,
            'NumOfProducts': NumOfProducts,
            'HasCrCard': HasCrCard,
            'IsActiveMember': IsActiveMember,
            'EstimatedSalary': EstimatedSalary
        }])

        # Transform with preprocessor
        processed_input = preprocessor.transform(input_df)

        # Predict
        prediction = model.predict(processed_input)[0]
        probability = model.predict_proba(processed_input)[0][1]

        result = "Churn" if prediction == 1 else "No Churn"

        return render_template(
            "index.html",
            prediction_text=f"Prediction: {result} (Probability: {probability:.2f})"
        )

    except Exception as e:
        return render_template("index.html", prediction_text=f"Input Error: {str(e)}")

# ------------------- MAIN -------------------
if __name__ == "__main__":
    app.run(debug=True)
