from flask import Flask, jsonify, request
from project_plant_crawler.database.base import db_session, DATABASE_PATH
import sqlite3
from project_plant_crawler.database.plant import Plant
from project_plant_crawler.database.month import Month



app = Flask(__name__)


def dict_factory(cursor, row):
    """
    Returns items from the database as dictionaries rather than lists, ie there will be keys in the data base
    """
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
def home():
    return """
    <h1>Beautiful vegetable garden</h1>
    <p>This site is a prototype API to help organizing your vegetable garden.</p>
    """


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/plants/all', methods=['GET'])
def api_plant_all():
def api_all():
    all_plants = []
    for plant in db_session.query(Plant).all():
        all_plants.append(plant.jsonify())
    return jsonify(all_plants)
    with sqlite3.connect(DATABASE_PATH) as conn:
        conn.row_factory = dict_factory  # Returns items from the database as dictionaries rather than lists
        cur = conn.cursor()
        all_plants = cur.execute('SELECT * FROM plants;').fetchall()
        return jsonify(all_plants)


@app.route('/api/v1/resources/plants', methods=['GET'])
def api_filter():

    query_parameters = request.args  # Get all arguments in the filter of the url

    # Collect arguments for each parameter separately
    name = query_parameters.get('name')
    family = query_parameters.get('family')

    # Base query: will look like that: SELECT <columns> FROM <table> WHERE <column=match> AND <column=match>;
    # The list to_filter will collect the parameters to be used in the query (so order matters)
    query = "SELECT * FROM plants WHERE"
    to_filter = []

    # For each type of parameter, adapt the query and add the parameter to the list of parameters
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if family:
        query += ' family=? AND'
        to_filter.append(family)
    if not (name or family):
        return page_not_found(404)

    query = query[:-4] + ';'  # Removes the last 'AND'

    with sqlite3.connect(DATABASE_PATH) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)