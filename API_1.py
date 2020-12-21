import flask
from flask import request, jsonify

# flask app
app = flask.Flask(__name__)

cars = [
    {'id': 0,
     'name': 'Lamborghini'},
    {'id': 1,
     'name': "Ferrari"}
]


# Home Route
@app.route('/', methods=['GET'])
def home():
    return "<h1>My First API</h1>"


@app.route('/car/', methods=['GET'])
def api():
    return jsonify(cars)


@app.route('/car/<id>', methods=['GET'])
def api_id(id):
    return jsonify(cars[int(id)])


app.run()