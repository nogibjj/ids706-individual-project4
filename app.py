# Basic Website Template
from flask import Flask, jsonify, request, render_template
import requests

OPENAI_API_KEY = ''

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize-text', methods=['POST'])
def summarize_text():
    data = request.json
    prompt = f"Summarize the following paragraph:\n\n{data['prompt']}\n\nSummary:"

    response = requests.post(
        'https://api.openai.com/v1/engines/text-davinci-003/completions',
        headers={
            'Authorization': f'Bearer {OPENAI_API_KEY}',
            'Content-Type': 'application/json'
        },
        json={
            'prompt': prompt,
            'max_tokens': 500
        },
        timeout=10  # 10 seconds timeout
    )

    print(response.json())  

    if response.status_code == 200:
        return jsonify(response.json()['choices'][0]['text'])
    else:
        return jsonify({'error': 'Error generating text'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
