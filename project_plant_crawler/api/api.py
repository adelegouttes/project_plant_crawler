from flask import Flask, jsonify, request
from project_plant_crawler.database.base import db_session
from project_plant_crawler.database.plant import Plant
from project_plant_crawler.database.month import Month
from project_plant_crawler.api.api_utilities import generate_filter_string


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
def page_not_found(e, message=None):
    main_message = """
        <h1>404</h1>
        <p>The resource could not be found.</p>
        """
    if message:
        return main_message + message, 404
    else:
        return main_message, 404


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/api/v1/resources/plants/all', methods=['GET'])
def api_plant_all():
    """A route to return all of the available plants in our catalog."""
    all_plants = []
    for plant in db_session.query(Plant).all():
        all_plants.append(plant.jsonify())
    return jsonify(all_plants)


@app.route('/api/v1/resources/plants', methods=['GET'])
def api_plant_filter():
    """A route to return only some plants, filtered by their name, family or ID"""

    query_parameters = request.args.to_dict()  # Get all arguments in the filter of the url

    allowed_keys = ['name', 'family', 'plant_id']
    try:
        to_filter = generate_filter_string(allowed_keys=allowed_keys,
                                           query_parameters=query_parameters)
    except KeyError as e_info:
        return page_not_found(404, message=e_info.args[0])

    plants = []
    for plant in db_session.query(Plant).filter(to_filter).all():
        plants.append(plant.jsonify())
    if len(plants) == 0:
        return page_not_found(404,
                              message='<p>Filtering is too restrictive: no plant matches all filters.</p>')
    return jsonify(plants)


@app.route('/api/v1/resources/months/all', methods=['GET'])
def api_month_all():
    """A route to return all of the available months in our catalog."""
    months = []
    for month in db_session.query(Month).all():
        months.append(month.jsonify())
    return jsonify(months)


@app.route('/api/v1/resources/months/harvest_months/all', methods=['GET'])
def api_month_harvest_month_all():
    """A route to return all of the plants gathered by harvest month."""
    harvest_months = []
    for month in db_session.query(Month).all():
        harvest_month = dict()
        harvest_month['month'] = month.jsonify()
        harvest_month['plants'] = []
        for plant in db_session.query(Plant).filter(Plant.harvest_months.contains(month)).all():
            harvest_month['plants'].append(plant.jsonify())
        harvest_months.append(harvest_month)
    return jsonify(harvest_months)


@app.route('/api/v1/resources/months/harvest_months', methods=['GET'])
def api_month_harvest_month_filter():
    """A route to return all of the plants gathered for one harvest month."""

    query_parameters = request.args.to_dict()  # Get all arguments in the filter of the url

    allowed_keys = ['month_id', 'month_name_eng']
    try:
        to_filter = generate_filter_string(allowed_keys=allowed_keys,
                                           query_parameters=query_parameters)
    except KeyError as e_info:
        return page_not_found(404, message=e_info.args[0])

    harvest_months = []
    for month in db_session.query(Month).filter(to_filter).all():
        harvest_month = dict()
        harvest_month['month'] = month.jsonify()
        harvest_month['plants'] = []
        for plant in db_session.query(Plant).filter(Plant.harvest_months.contains(month)).all():
            harvest_month['plants'].append(plant.jsonify())
        if len(harvest_month['plants']) == 0:
            return page_not_found(404,
                                  message='<p>Filtering is too restrictive: no plants for this harvest month.</p>')
        harvest_months.append(harvest_month)
    if len(harvest_months) == 0:
        return page_not_found(404,
                              message='<p>Filtering is too restrictive: no harvest month for filter.</p>')

    return jsonify(harvest_months)


if __name__ == '__main__':
    app.run(debug=True)