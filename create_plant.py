import json


class Plant(object):
    """Plant is defined by it's name, code, family and description"""
    def __init__(self, plant_dict):
        self._name = plant_dict['name']
        self._code = plant_dict['code']
        self._family = plant_dict['family']
        self._description_raw = plant_dict['description']
        self._description_cleaned = plant_dict['description']

    def __repr__(self):
        return 'Plant: name({name}), code({code}), family({family}), description({description})'\
                .format(name=self._name, code=self._code, family=self._family, description='{...}')

    def filter_description_by_key(self, keys: list):
        """In the attribute _description, keep only some of the original information.
        Meaning, the dictionary will have all the keys that are note listed in the 'keys' parameter filtered out"""
        print('Filtering description to contain only: {}'.format(', '.join(keys)))
        description = self._description_cleaned
        self._description_cleaned = {key: description[key] for key in description if key in keys}

    def get_period_seedling(self):
        period_seedling_direct = self._description_raw['periode_semis_terre']
        period_seedling_shelter = self._description_raw['periode_semis_abri']
        print(period_seedling_direct)
        print(period_seedling_shelter)

    @property
    def name(self):
        return self._name

    @property
    def code(self):
        return self._code

    @property
    def family(self):
        return self._family

    @property
    def description_raw(self):
        return self._description_raw

    @property
    def description_cleaned(self):
        return self._description_cleaned

    @description_cleaned.setter
    def description_cleaned(self, new_description):
        self._description_cleaned = new_description


def main():

    with open('./data/product_info.json') as file:
        data = json.load(file)

    plant_codes = list(data.keys())
    print(plant_codes)
    # print(data[plant_codes[0]])
    my_plant = data[plant_codes[0]]
    my_plant = Plant(my_plant)
    print(my_plant)

    print(my_plant.description_raw.keys())

    my_plant.filter_description_by_key(keys=['semis_variete', 'conseil_semis'])
    print(my_plant.description_raw)

    my_plant.get_period_seedling()


if __name__ == '__main__':
    main()
