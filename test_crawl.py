import unittest
import requests
import json


class ProductLinkTest(unittest.TestCase):
    def setUp(self):
        #TODO write file name somewhere else??
        self.product_url_list = []
        with open('product_link_file.json') as link_file:
            product_url_list = json.load(link_file)
            self.product_url_list = product_url_list

    def test_mother_url_exists(self):
        #TODO write the url somewhere else??
        page_link = 'https://kokopelli-semences.fr/fr/c/semences/potageres'
        page_response = requests.get(page_link, timeout=5)
        self.assertEqual(page_response.status_code, 200)

    def test_product_link_json_is_list(self):
        self.assertIsInstance(self.product_url_list, list)

    def test_product_link_json_not_empty(self):
        self.assertNotEqual(self.product_url_list, [])

    def test_product_link_json_contains_strings_only(self):
        #TODO proper way to test list content
        not_a_string = [n for n in self.product_url_list if not isinstance(n, str)]
        self.assertEqual(not_a_string, [])


class ProductInfoTest(unittest.TestCase):
    def setUp(self):
        #TODO write file name somewhere else??
        self.product_info = []
        with open('product_info.json') as file:
            product_info = json.load(file)
            self.product_info = product_info

    def test_product_info_is_dict(self):
        self.assertIsInstance(self.product_info, dict)

    def test_product_info_is_not_empty(self):
        self.assertNotEqual(self.product_info, {})

    def test_product_info_check_keys(self):
        for key in self.product_info:
            plant = self.product_info[key]
            self.assertEqual(list(plant.keys()), ['code', 'name', 'family', 'description'])

    def test_product_info_check_description(self):
        for key in self.product_info:
            plant = self.product_info[key]
            self.assertIsInstance(plant['description'], dict)


if __name__ == '__main__':
    unittest.main()