from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/test', methods=['GET', 'POST'])
def test():
    return jsonify({"message": "Test endpoint"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)