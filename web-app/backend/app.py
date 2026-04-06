from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
from utils import preprocess_data, make_prediction
import os

app = Flask(__name__)
CORS(app)

# Load ML model
MODEL_PATH = 'model.pkl'
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
else:
    model = None
    print("Warning: Model file not found. ML features will be unavailable.")

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Prism Insurance Analysis API'})

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """Analyze uploaded CSV file"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.csv'):
            return jsonify({'error': 'File must be CSV format'}), 400
        
        # Read CSV
        df = pd.read_csv(file)
        
        # Preprocess data
        processed_data = preprocess_data(df)
        
        # Make prediction if model is available
        result = {
            'rows': len(df),
            'columns': list(df.columns),
            'summary': processed_data.describe().to_dict()
        }
        
        if model is not None:
            predictions = make_prediction(model, processed_data)
            result['predictions'] = predictions
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
