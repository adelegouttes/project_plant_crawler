import unittest
import requests
import json
from project_plant_crawler.crawl.constants import MAIN_URL, CRAWL_OUTPUT_PRODUCT_LINKS_PATH, \
    CRAWL_OUTPUT_PRODUCT_DESCRIPTION_PATH


class ProductLinkTest(unittest.TestCase):
    def setUp(self):
        self.product_url_list = []
        with open(CRAWL_OUTPUT_PRODUCT_LINKS_PATH) as link_file:
            product_url_list = json.load(link_file)
            self.product_url_list = product_url_list

    def test_mother_url_exists(self):
        page_link = MAIN_URL
        page_response = requests.get(page_link, timeout=5)
        self.assertEqual(page_response.status_code, 200)

    def test_product_link_json_is_list(self):
        self.assertIsInstance(self.product_url_list, list)

    def test_product_link_json_not_empty(self):
        self.assertNotEqual(self.product_url_list, [])

    def test_product_link_json_contains_strings_only(self):
        not_a_string = [n for n in self.product_url_list if not isinstance(n, str)]
        self.assertFalse(not_a_string)


class ProductInfoTest(unittest.TestCase):
    def setUp(self):
        self.product_info = []
        with open(CRAWL_OUTPUT_PRODUCT_DESCRIPTION_PATH) as file:
            product_info = json.load(file)
            self.product_info = product_info

    def test_product_info_is_dict(self):
        self.assertIsInstance(self.product_info, dict)

    def test_product_info_is_not_empty(self):
        self.assertTrue(self.product_info, {})

    def test_product_info_check_keys(self):
        for key in self.product_info:
            plant = self.product_info[key]
            self.assertEqual(list(plant.keys()),
                             ['code', 'name', 'family',
                              'period_harvest', 'period_seedling_direct', 'period_seedling_shelter',
                              'description_raw']
                             )

    def test_product_info_check_description(self):
        for key in self.product_info:
            plant = self.product_info[key]
            self.assertIsInstance(plant['description_raw'], dict)


if __name__ == '__main__':
    unittest.main()