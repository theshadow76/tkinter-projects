# search products at amazon.com
def search_products(keyword):
    import requests
    from bs4 import BeautifulSoup
    import re
    import json
    import time
    import random
    import os
    import sys
    import cgi
    import cgitb
    cgitb.enable()
    # get the html page
    url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + keyword
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    html = response.text
    # parse the html page
    soup = BeautifulSoup(html, 'html.parser')
    # get the product list
    product_list = soup.find_all('div', class_='s-item-container')
    # get the product information
    product_info = []
    for product in product_list:
        # get the product title
        title = product.find('h2', class_='a-size-medium s-inline s-access-title a-text-normal').text
        # get the product price
        price = product.find('span', class_='a-offscreen').text
        # get the product rating
        rating = product.find('span', class_='a-icon-alt').text
        # get the product review
        review = product.find('a', class_='a-size-small a-link-normal').text
        # get the product link
        link = product.find('a', class_='a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal')['href']
        # get the product image
        image = product.find('img', class_='s-access-image cfMarker')['src']
        # get the product asin
        asin = re.search('/([A-Z0-9]{10})/', link).group(1)
        # get the product category
        category = re.search('/([A-Z0-9]{10})/', link).group(1)
        # get the product brand
        brand = re.search('/([A-Z0-9]{10})/', link).group(1)
        # get the product description
        description = product.find('div', class_='a-row a-spacing-mini').text
        print(title, price, rating, review, link, image, asin, category, brand, description)
search_products("pc")