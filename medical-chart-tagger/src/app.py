from flask import Flask, request, jsonify
import yaml
from models.tagger import Tagger

app = Flask(__name__)

# Load configuration
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Initialize the Tagger model
tagger = Tagger(config['model_parameters'])

@app.route('/tag', methods=['POST'])
def tag_medical_chart():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    tags = tagger.predict(text)
    return jsonify({'tags': tags})

if __name__ == '__main__':
    app.run(debug=True)