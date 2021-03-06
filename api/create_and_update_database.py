from models import Plant
import database
import json


def main():
    database.init_db()

    with open('../data/product_info.json') as file:
        plants = json.load(file)

    plant_codes = list(plants.keys())
    for code in plant_codes:
        plant = plants[code]
        plant_entry = Plant(code=plant['code'],
                            name=plant['name'],
                            family=plant['family'],
                            # description_raw=plant['description_raw']
                            )
        database.db_session.add(plant_entry)
        database.db_session.commit()
        print(plant_entry)


if __name__ == '__main__':
    main()
