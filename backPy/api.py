from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])
def api():
    data = {'message': 'Hello, API!'}
    return jsonify(data)


@app.route('/', methods=['GET'])
def hello():
    return render_template('hello.html')


@app.route('/page2', methods=['GET'])
def page2():
    return render_template('page2.html')


if __name__ == '__main__':
    app.run()
