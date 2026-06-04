from bs4 import BeautifulSoup

from shopping_ai.discovery.product_parser import (
    ProductParser
)

with open(
    "sample_card.html",
    "r",
    encoding="utf-8"
) as file:

    html = file.read()

soup = BeautifulSoup(
    html,
    "lxml"
)

card = soup.select_one(
    "li.product-base"
)

parser = ProductParser()

product = parser.parse(
    card
)

print(product)