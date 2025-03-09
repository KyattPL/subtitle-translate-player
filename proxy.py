from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, origins=["https://kyattpl.github.io"])  # Allow only your GitHub Pages site

LIBRETRANSLATE_URL = "http://localhost:5000"  # Your running LibreTranslate instance

@app.route('/translate', methods=['POST', 'OPTIONS'])
def translate():
    if request.method == 'OPTIONS':
        # Handle CORS preflight
        response = jsonify({"message": "CORS preflight passed"})
        response.headers["Access-Control-Allow-Origin"] = "https://kyattpl.github.io"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    # Forward request to LibreTranslate
    response = requests.post(f"{LIBRETRANSLATE_URL}/translate", json=request.json)

    # Modify response headers
    modified_response = jsonify(response.json())
    modified_response.headers["Access-Control-Allow-Origin"] = "https://kyattpl.github.io"
    return modified_response

if __name__ == '__main__':
    app.run(port=5050)  # Runs on localhost:5050