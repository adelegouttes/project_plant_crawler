from bs4 import BeautifulSoup
import requests
import time
import json
import logging


def get_product_links_from_a_page(page_url:str):
    """From a page with a list of plants, get the url of each plant"""
    page_link = page_url
    page_response = requests.get(page_link, timeout=5)
    if page_response.status_code != 200:
        raise ValueError('Page does not exist: {}'.format(page_url))
    page_content = BeautifulSoup(page_response.content, "html.parser")

    product_grid = page_content.findAll("a", attrs={'class': 'product__readmore'})
    product_links = []
    for g in range(len(product_grid)):
        link = product_grid[g]['href']
        product_links.append(link)

    return product_links


def get_product_links_from_all_pages(main_url: str, page_from=1, page_to=2):
    """Takes all pages between page_from and page_to, returns a list of all the product links in those pages."""
    pages = range(page_from, page_to)
    product_links = []
    for p in pages:
        time.sleep(1)
        page_url = main_url + '?page=' + str(p)
        try:
            new_links = get_product_links_from_a_page(page_url=page_url)
            product_links += new_links
        except ValueError:
            logging.warning('Link collection stopped at page {}'.format(p))
            return product_links

    return product_links


def main():
    product_links = get_product_links_from_all_pages(main_url='https://kokopelli-semences.fr/fr/c/semences/potageres',
                                                 page_from=1, page_to=5)
    with open('product_link_file.json', mode='w') as file:
        json.dump(product_links, file)


if __name__ == "__main__":
    main()


