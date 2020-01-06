from project_plant_crawler.database.base import db_session
from project_plant_crawler.database.plant import Plant
from project_plant_crawler.database.month import Month
from sqlalchemy.orm.attributes import InstrumentedAttribute


def generate_filter_string(allowed_keys: list, query_parameters: dict):
    """Takes the filters required when calling the api,
    checks whether all required filters are allowed,
    and generates a string to be used when querying Plant table in the database"""
    filter_string = ''
    if not all(parameter in allowed_keys for parameter in query_parameters.keys()):
        allowed_keys_string = ', '.join(str(i) for i in allowed_keys)
        raise KeyError('<p>Please filter plants only with the following arguments: {}.</p>'
                       .format(allowed_keys_string))
    for key in query_parameters.keys():
        value = query_parameters[key]
        filter_string += " {}='{}' AND".format(key, value)
    return filter_string[:-4]  # Removes the last 'AND'


def generate_plants_for_month_list(months: list,
                                   plant_month_attribute: InstrumentedAttribute):
    month_results = []
    for month in months:
        month_result = dict()
        month_result['month'] = month.jsonify()
        month_result['plants'] = []
        for plant in db_session.query(Plant).filter(plant_month_attribute.contains(month)).all():
            month_result['plants'].append(plant.jsonify())
        if len(month_result['plants']) == 0:
            return ValueError('<p>Filtering is too restrictive: no plants for this harvest month.</p>')
        month_results.append(month_result)
    return month_results

