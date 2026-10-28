from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# ===== Feature names & placeholders (30) =====
FEATURES = [
    "mean radius","mean texture","mean perimeter","mean area","mean smoothness",
    "mean compactness","mean concavity","mean concave points","mean symmetry","mean fractal dimension",
    "radius error","texture error","perimeter error","area error","smoothness error",
    "compactness error","concavity error","concave points error","symmetry error","fractal dimension error",
    "worst radius","worst texture","worst perimeter","worst area","worst smoothness",
    "worst compactness","worst concavity","worst concave points","worst symmetry","worst fractal dimension"
]

PLACEHOLDERS = [
    14.5,19.3,92.0,654.5,0.10,
    0.15,0.20,0.09,0.18,0.060,
    0.5,1.2,3.5,20.0,0.010,
    0.020,0.030,0.010,0.020,0.004,
    16.0,25.0,110.0,880.0,0.140,
    0.25,0.30,0.12,0.25,0.080
]

FEATURE_PAIRS = list(zip(FEATURES, PLACEHOLDERS))

# ===== Load trained model =====
# Adjust the path if your model is elsewhere (e.g., 'model.pkl')
MODEL_PATH = 'models/model.pkl'
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html', feature_pairs=FEATURE_PAIRS)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        values = []
        missing = []
        bad = []

        # Read each feature by name in the SAME ORDER
        for name in FEATURES:
            raw = request.form.get(name, '').strip()
            if raw == '':
                missing.append(name)
                continue
            # allow commas as decimal separators
            raw = raw.replace(',', '.')
            try:
                values.append(float(raw))
            except ValueError:
                bad.append((name, raw))

        if missing or bad:
            msg_parts = []
            if missing:
                msg_parts.append(f"Missing fields: {', '.join(missing)}")
            if bad:
                bad_fields = ', '.join([f"{n}='{v}'" for n, v in bad])
                msg_parts.append(f"Non-numeric values: {bad_fields}")
            message = "Error: " + " | ".join(msg_parts)
            return render_template('index.html',
                                   feature_pairs=FEATURE_PAIRS,
                                   prediction=message, label="Error")

        if len(values) != 30:
            return render_template('index.html',
                                   feature_pairs=FEATURE_PAIRS,
                                   prediction=f"Error: Expected 30 values, got {len(values)}.",
                                   label="Error")

        arr = np.array(values, dtype=float).reshape(1, -1)

        pred = model.predict(arr)
        if pred[0] == 1:
            result = "⚠️ The tumor is Malignant (Cancerous). Please consult a doctor."
            label = "Cancerous"
        else:
            result = "✅ The tumor is Benign (Non-Cancerous). You are safe."
            label = "Non-Cancerous"

        return render_template('index.html',
                               feature_pairs=FEATURE_PAIRS,
                               prediction=result, label=label)

    except Exception as e:
        return render_template('index.html',
                               feature_pairs=FEATURE_PAIRS,
                               prediction=f"Error: Invalid input. Please enter valid numbers. ({e})",
                               label="Error")

if __name__ == '__main__':
    app.run(debug=True)
