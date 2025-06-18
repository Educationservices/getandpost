from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

current_text = ""
server_text = None
case_data = None
base64_music = None
flag_value = None  # Stores True/False flag

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
    global case_data
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'text1' not in data or 'text2' not in data:
            return jsonify({'error': 'Missing "text1" or "text2" in JSON body'}), 400
        case_data = {
            'text1': data['text1'],
            'text2': data['text2']
        }
        return jsonify({'message': 'Case data updated', 'data': case_data})
    if case_data is None:
        return jsonify(False)
    return jsonify(case_data)

@app.route('/base64music', methods=['GET', 'POST'])
def base64music_handler():
    global base64_music
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'base64' not in data:
            return jsonify({'error': 'Missing "base64" in JSON body'}), 400
        base64_music = data['base64']
        return jsonify({'message': 'Base64 music data updated'})
    if base64_music is None:
        return jsonify(False)
    return jsonify({'base64': base64_music})

@app.route('/flag', methods=['GET', 'POST'])
def flag_handler():
    global flag_value
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'flag' not in data:
            return jsonify({'error': 'Missing "flag" in JSON body'}), 400
        if not isinstance(data['flag'], bool):
            return jsonify({'error': '"flag" must be true or false'}), 400
        flag_value = data['flag']
        return jsonify({'message': 'Flag updated', 'flag': flag_value})
    if flag_value is None:
        return jsonify(False)
    return jsonify({'flag': flag_value})

@app.route('/', methods=['GET'])
def root_handler():
    return jsonify({'message': 'Service running. Use /text, /server, /case, /base64music, or /flag endpoints.'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
