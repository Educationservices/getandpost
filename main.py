from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

current_text = ""

@app.route('/text', methods=['GET', 'POST'])
def text_handler():
    global current_text
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Missing "text" in JSON body'}), 400
        current_text = data['text']
        return jsonify({'message': 'Text updated', 'text': current_text})
    # For GET request
    return jsonify({'text': current_text})

@app.route('/', methods=['GET'])
def root_handler():
    return jsonify({'message': 'Service running. Use /text endpoint.'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use env PORT or default 5000
    app.run(host='0.0.0.0', port=port)
