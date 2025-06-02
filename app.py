from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load('models/model.pkl')
scaler = joblib.load('models/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[key]) for key in request.form]
        scaled_features = scaler.transform([features])
        prediction = model.predict(scaled_features)

        result = 'High Risk of Heart Disease' if prediction[0] == 1 else 'Low Risk of Heart Disease'
        return render_template('index.html', prediction=result)

    except Exception as e:
        return f"Error: {e}"
    
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)