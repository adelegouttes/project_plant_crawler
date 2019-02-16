from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/')
def home():
    return """
    <h1>Beautiful vegetable garden</h1>
    <p>This site is a prototype API to help organizing your vegetable garden.</p>
    """


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/plants/all', methods=['GET'])
def api_all():
    return jsonify(plants)





if __name__ == '__main__':
    with open('../data/product_info.json') as file:
        plants = json.load(file)
    app.run(debug=True)