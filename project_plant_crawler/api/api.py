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
    all_plants = []
    for plant in db_session.query(Plant).all():
        all_plants.append(plant.jsonify())
    return jsonify(all_plants)


@app.route('/api/v1/resources/plants', methods=['GET'])
def api_plant_filter():

    query_parameters = request.args  # Get all arguments in the filter of the url

    # Collect arguments for each parameter separately
    name = query_parameters.get('name')
    family = query_parameters.get('family')
    plant_id = query_parameters.get('plant_id')

    # For each type of parameter, adapt the query and add the parameter to the list of parameters
    to_filter = ''
    if name:
        to_filter += ' name=%r AND' % name
    if family:
        to_filter += ' family=%r AND' % family
    if plant_id:
        to_filter += ' plant_id=%r AND' % plant_id
    if not (name or family or plant_id):
        return page_not_found(404)

    to_filter = to_filter[:-4]  # Removes the last 'AND'

    plants = []
    for plant in db_session.query(Plant).filter(to_filter).all():
        plants.append(plant.jsonify())
    if len(plants)==0:
        return page_not_found(404)
    return jsonify(plants)


if __name__ == '__main__':
    app.run(debug=True)