from flask import Flask, request, jsonify, render_template
import joblib
import os

app = Flask(__name__)

# Load the trained model and encoder
MODEL_PATH = 'models/fraud_detection_model.joblib'
ENCODER_PATH = 'models/type_encoder.joblib'

if not os.path.exists(MODEL_PATH) or not os.path.exists(ENCODER_PATH):
    raise FileNotFoundError("Model or encoder file not found. Ensure the model is trained and saved.")

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

# Route to serve the frontend
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.json
        step = int(data['step'])
        txn_type = data['type']
        amount = float(data['amount'])
        oldbalanceOrg = float(data['oldbalanceOrg'])
        newbalanceOrig = float(data['newbalanceOrig'])
        oldbalanceDest = float(data['oldbalanceDest'])
        newbalanceDest = float(data['newbalanceDest'])

        # Encode the transaction type
        type_encoded = encoder.transform([txn_type])[0]

        # Prepare the input features for the model
        features = [[step, type_encoded, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]]

        # Predict using the trained model
        prediction = model.predict(features)[0]

        # Return the prediction result
        return jsonify({'isFraud': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
