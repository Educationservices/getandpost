from flask import Flask, request, jsonify

app = Flask(__name__)


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
    
    if request.method == 'GET':
        return jsonify({'text': current_text})

if __name__ == '__main__':
    app.run(debug=True)
