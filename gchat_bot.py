from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def on_event():
    event = request.get_json()
    if event['type'] == 'MESSAGE':
        text = event['message']['text']
        if text.lower() == 'open a new tab':
            
            return jsonify({'text': 'Opening a new tab...'})
        else:
            return jsonify({'text': 'Unrecognized command'})

if __name__ == '__main__':
    app.run(port=8080)
