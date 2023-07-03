from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    data = {'message': 'Hello, API!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run()