# Sample routes.py content
from flask import Flask, request, jsonify
from mileage_ocr import extract_mileage

app = Flask(__name__)

@app.route('/extract-mileage', methods=['POST'])
def extract_mileage_route():
    file = request.files['image']
    mileage = extract_mileage(file)
    return jsonify({'mileage': mileage})

if __name__ == '__main__':
    app.run(debug=True)