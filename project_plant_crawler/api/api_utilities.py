
def generate_filter_string(allowed_keys: list, query_parameters: dict):

    filter_string = ''
    for key in allowed_keys:
        try:
            value = query_parameters[key]
        except KeyError:
            value = None
        if value:
            filter_string += " {}='{}' AND".format(key, value)
    if filter_string == '':
        return ''
    else:
        return filter_string[:-4]  # Removes the last 'AND'


