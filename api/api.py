from flask import Flask, jsonify, request
import json
from database import db_session, init_db
from models import Plant

import os


print(os.path.abspath(os.path.dirname(__file__)))

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


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()
    with open('../data/product_info.json') as file:
        plants = json.load(file)
    app.run(debug=True)