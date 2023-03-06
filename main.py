import requests
from bs4 import BeautifulSoup as bs
import json


def get_category_blocks(ramen) -> list:
    category_blocks = []
    try:
        for el in ramen.findAll(class_="category"):
            category_blocks.append(el)
    except:
        ...
    return category_blocks


def parse_category_blocks(category_blocks: list) -> dict:
    products = {}
    try:
        for block in category_blocks:
            for category in block.findAll(class_="category-name"):
                names = block.findAll(class_="name")
                descriptions = block.findAll(class_="text-description")
                prices = block.findAll(class_="price")
                for i in range(0, len(names)):
                    products[f"{category.text.strip()}"] = {"Название": f"{names[i].text.strip()}",
                                                             "Описание": f"{descriptions[i].text.strip()}",
                                                             "Цена": f"{prices[i].text.strip()}"}
    except:
        ...
    return products



def main(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/110.0.0.0 Safari/537.36 '
    }
    page = requests.get(url, headers=headers)
    ramen = bs(page.text, "html.parser")
    category_blocks = get_category_blocks(ramen)
    products = parse_category_blocks(category_blocks)
    print(products)



if __name__ == '__main__':
    main('https://pizzamia.smartomato.ru/')
