import os

MAIN_URL = 'https://kokopelli-semences.fr/fr/c/semences/potageres'

abs_file_path = os.path.dirname(os.path.abspath(__file__))

CRAWL_OUTPUT_PATH = os.path.dirname(abs_file_path) + '/data'

CRAWL_OUTPUT_PRODUCT_LINKS_NAME = 'product_link_file.json'
CRAWL_OUTPUT_PRODUCT_LINKS_PATH = os.path.join(CRAWL_OUTPUT_PATH, CRAWL_OUTPUT_PRODUCT_LINKS_NAME)

CRAWL_OUTPUT_PRODUCT_DESCRIPTION_NAME = 'product_info.json'
CRAWL_OUTPUT_PRODUCT_DESCRIPTION_PATH = os.path.join(CRAWL_OUTPUT_PATH, CRAWL_OUTPUT_PRODUCT_DESCRIPTION_NAME)

