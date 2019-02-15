

def format_period(period_string):
    """Transform a string enumerating months in French to a list object of integer between 1 and 12."""

    translation_month = {'Janvier': 1, 'Février':2, 'Mars': 3, 'Avril': 4, 'Mai': 5, 'Juin': 6, 'Juillet': 7,
                         'Août': 8, 'Septembre': 9, 'Octobre': 10, 'Novembre': 11, 'Décembre': 12}
    period_formatted = period_string.split(', ')
    period_formatted = [translation_month[month] for month in period_formatted]

    return period_formatted


def get_period_seedling(product_description):

    print(product_description.keys())
    try:
        period_seedling_direct = format_period(product_description['periode_semis_terre'])
    except KeyError:
        period_seedling_direct = []

    try:
        period_seedling_shelter = format_period(product_description['periode_semis_abri'])
    except KeyError:
        period_seedling_shelter = []

    try:
        period_harvest = format_period(product_description['periode_recolte'])
    except KeyError:
        period_harvest = []

    print(period_seedling_direct)
    print(period_seedling_shelter)
    print(period_harvest)

