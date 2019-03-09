from project_plant_crawler.database.plant import Plant
from project_plant_crawler.database.month import Month
from project_plant_crawler.database.base import init_db, db_session
import json
from project_plant_crawler.crawl.constants import CRAWL_OUTPUT_PRODUCT_DESCRIPTION_PATH


def fill_month_table():
    """Create a table in database with 12 months"""

    db_session.query(Month).delete()

    # Add the 12 months manually
    db_session.add(Month(month_id=1, month_name_eng='January'))
    db_session.add(Month(month_id=2, month_name_eng='February'))
    db_session.add(Month(month_id=3, month_name_eng='March'))
    db_session.add(Month(month_id=4, month_name_eng='April'))
    db_session.add(Month(month_id=5, month_name_eng='May'))
    db_session.add(Month(month_id=6, month_name_eng='June'))

    db_session.add(Month(month_id=7, month_name_eng='July'))
    db_session.add(Month(month_id=8, month_name_eng='August'))
    db_session.add(Month(month_id=9, month_name_eng='September'))
    db_session.add(Month(month_id=10, month_name_eng='October'))
    db_session.add(Month(month_id=11, month_name_eng='November'))
    db_session.add(Month(month_id=12, month_name_eng='December'))

    db_session.commit()


def fill_plant_associated_month_table(plant_raw: dict,  input_key: str):
    inputs = plant_raw[input_key]
    return db_session.query(Month).filter(Month.month_id.in_(inputs)).all()


def fill_plant_table(data_source_path):

    db_session.query(Plant).delete()

    # Read json where crawl data is stored
    with open(data_source_path) as file:
        plants = json.load(file)

    # For each plant: create a plant entry, and corresponding harvest months
    plant_codes = list(plants.keys())
    for code in plant_codes:

        # Create plant
        plant = plants[code]
        plant_entry = Plant(plant_id=plant['code'],
                            name=plant['name'],
                            family=plant['family'],
                            )
        db_session.add(plant_entry)

        # Update harvest month for that table
        harvest_month_ids = plant['period_harvest']
        plant_entry.harvest_months = db_session.query(Month)\
                                                .filter(Month.month_id.in_(harvest_month_ids))\
                                                .all()

        # plant_entry.seedling_direct_months = fill_plant_associated_month_table(plant_raw=plant,
        #                                                                        input_key='period_seedling_direct')
        # seedling_direct_month_ids = plant['period_seedling_direct']
        # plant_entry.seedling_direct_months = db_session.query(Month)\
        #                                         .filter(Month.month_id.in_(seedling_direct_month_ids))\
        #                                         .all()

    db_session.commit()


def main():

    init_db()
    fill_month_table()
    fill_plant_table(data_source_path=CRAWL_OUTPUT_PRODUCT_DESCRIPTION_PATH)
    db_session.close()




if __name__ == '__main__':
    main()
