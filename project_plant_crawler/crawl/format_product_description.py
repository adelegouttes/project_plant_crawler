import logging


def format_period_string(period_string):
    """Transform a string enumerating months in French to a list object of integer between 1 and 12."""

    translation_month = {'Janvier': 1, 'Février':2, 'Mars': 3, 'Avril': 4, 'Mai': 5, 'Juin': 6, 'Juillet': 7,
                         'Août': 8, 'Septembre': 9, 'Octobre': 10, 'Novembre': 11, 'Décembre': 12}
    period_formatted = period_string.split(', ')
    period_formatted = [translation_month[month] for month in period_formatted]

    return period_formatted


def get_and_format_period(product_description, key, format_function=format_period_string):
    """For a period key in product description, apply a transformation.
    When the key does not exist, return an empty list """

    try:
        period = format_function(product_description[key])
    except KeyError as e:
        logging.warning("KeyError: %s" % e)
        return []

    return period

