from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

current_text = ""
server_text = None
case_text = None

@app.route('/text', methods=['GET', 'POST'])
def text_handler():
    global current_text
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Missing "text" in JSON body'}), 400
        current_text = data['text']
        return jsonify({'message': 'Text updated', 'text': current_text})
    return jsonify({'text': current_text})

@app.route('/server', methods=['GET', 'POST'])
def server_handler():
    global server_text
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Missing "text" in JSON body'}), 400
        server_text = data['text']
        return jsonify({'message': 'Server text updated', 'text': server_text})
    if server_text is None:
        return jsonify(False)
    return jsonify({'text': server_text})

@app.route('/case', methods=['GET', 'POST'])
def case_handler():
    global case_text
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Missing "text" in JSON body'}), 400
        case_text = data['text']
        return jsonify({'message': 'Case text updated', 'text': case_text})
    if case_text is None:
        return jsonify(False)
    return jsonify({'text': case_text})

@app.route('/', methods=['GET'])
def root_handler():
    return jsonify({'message': 'Service running. Use /text, /server, or /case endpoints.'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
