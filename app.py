from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/check/endpoint', methods=['GET'])
def check_endpoint():
    return jsonify({"status": "Running smoothly"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
