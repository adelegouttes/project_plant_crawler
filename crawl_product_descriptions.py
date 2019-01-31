from bs4 import BeautifulSoup
import requests
import json
import time
import crawl_product_links

def get_product_info(product_url: str):
    """From a unique plant URL, get the plant name, family and culture description"""

    page_link = product_url
    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    # Main description of the product
    product_description = page_content.findAll("div", attrs={"class": "product__description"})[0]
    product_code = product_description.findAll("span", attrs={"class": "product__reference"})[0].span.text
    product_name = product_description.h1.text
    product_family = product_description.findAll("div", attrs={"class": "product__family"})[0].text

    # Details about the product
    product_description = {}
    product_attributes = page_content.findAll("div", attrs={"class": "tabs-content__row"})
    for a in range(len(product_attributes)):
        attribute = product_attributes[a]
        attribute_key = attribute.label['for']
        attribute_text = attribute.p.text
        product_description[attribute_key] = attribute_text

    # Shape final output
    product_data = {'code': product_code,
                    'name': product_name,
                    'family': product_family,
                    'description': product_description}

    return product_data

def get_all_product_info(product_url_list: list):

    result = {}
    for product_url in product_url_list:
        time.sleep(0.1)
        product_info = get_product_info(product_url=product_url)
        product_code = product_info['code']
        result[product_code] = product_info

    return result

def main():
    product_url_list = crawl_product_links.get_product_links_from_all_pages(
                                        main_url='https://kokopelli-semences.fr/fr/c/semences/potageres',
                                        page_from=1, page_to=2)
    result = get_all_product_info(product_url_list=product_url_list)
    with open('product_info.json', mode='w') as file:
        json.dump(result, file)


if __name__ == "__main__":
    main()
