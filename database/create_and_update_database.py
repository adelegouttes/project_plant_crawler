from plant import Plant
from base import init_db, db_session
import json


def main():
    init_db()
    db_session.query(Plant).delete()


    with open('../data/product_info.json') as file:
        plants = json.load(file)

    plant_codes = list(plants.keys())
    for code in plant_codes:
        plant = plants[code]
        plant_entry = Plant(code=plant['code'],
                            name=plant['name'],
                            family=plant['family'],
                            )
        db_session.add(plant_entry)

        print(plant_entry)

    db_session.commit()
    db_session.close()


if __name__ == '__main__':
    main()
