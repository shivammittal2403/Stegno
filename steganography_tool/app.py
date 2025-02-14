from flask import Flask, request, jsonify
from steganography import Steganography
from ai_model import classify_data

app = Flask(__name__)

@app.route('/embed', methods=['POST'])
def embed_data():
    """Endpoint to embed data into an image."""
    data = request.json
    image_path = data['image_path']
    secret_message = data['secret_message']
    
    steganography = Steganography(image_path)
    result_image = steganography.embed(secret_message)
    
    return jsonify({"result_image": result_image})

@app.route('/extract', methods=['POST'])
def extract_data():
    """Endpoint to extract data from an image."""
    data = request.json
    image_path = data['image_path']
    
    steganography = Steganography(image_path)
    secret_message = steganography.extract()
    
    return jsonify({"secret_message": secret_message})

@app.route('/classify', methods=['POST'])
def classify():
    """Endpoint to classify data using AI model."""
    data = request.json
    input_data = data['input_data']
    
    result = classify_data(input_data)
    
    return jsonify({"classification": result})

if __name__ == '__main__':
    app.run(debug=True)
