from flask import Flask, request, render_template
import numpy as np
import pickle
import sklearn

print("Sklearn version:", sklearn.__version__)

# Load models
dtr = pickle.load(open('models/dtr.pkl', 'rb'))
preprocessor = pickle.load(open('models/preprocessor.pkl', 'rb'))

# Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get form inputs and strip whitespace
            Year = request.form['Year'].strip()
            average_rain_fall_mm_per_year = request.form['average_rain_fall_mm_per_year'].strip()
            pesticides_tonnes = request.form['pesticides_tonnes'].strip()
            avg_temp = request.form['avg_temp'].strip()
            Area = request.form['Area'].strip()      # categorical
            Item = request.form['Item'].strip()      # categorical

            # Convert only numeric inputs
            numeric_features = [
                float(Year),
                float(average_rain_fall_mm_per_year),
                float(pesticides_tonnes),
                float(avg_temp)
            ]

            # Combine numeric and categorical features
            features = np.array([numeric_features + [Area, Item]], dtype=object)

            # Transform features and predict
            transformed_features = preprocessor.transform(features)
            prediction = dtr.predict(transformed_features)[0]

            return render_template('index.html', prediction=f"Predicted Yield: {prediction}")

        except ValueError as e:
            return render_template('index.html', prediction=f"Input Error: {e}")

        except Exception as e:
            return render_template('index.html', prediction=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
