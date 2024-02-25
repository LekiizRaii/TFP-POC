"""This file is used to connect our model with the system server"""
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

path_to_TFP_model = '/somedir'

# Load pre-trained TFP model
model = tf.keras.models.load_model(path_to_TFP_model)

@app.route('/predict', methods=['POST'])
def predict():
    """This method will return the result of predicting process from given traffic data"""
    # Get traffic data from the request
    traffic_data = request.json
    
    # Preprocess the traffic data
    preprocessed_traffic_data = preprocess_traffic_data(traffic_data)

    # Make prediction
    prediction = model.predict(np.array([preprocessed_traffic_data]))
    
    # Return the prediction as JSON
    return jsonify({'predicted_congestion_level': float(prediction)})

def preprocess_traffic_data(traffic_data):
    """Conduct the data preprocessing process"""
    pass

if __name__ == '__main__':
    app.run(debug=True)
