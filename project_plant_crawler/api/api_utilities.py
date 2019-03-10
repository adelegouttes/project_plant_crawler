
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


