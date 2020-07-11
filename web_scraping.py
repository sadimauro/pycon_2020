#!/usr/bin/env python3

"""
https://us.pycon.org/2020/schedule/presentation/72/
https://colab.research.google.com/drive/1_8F6NgmIIsob5fWwEzDiDbDlRPbo5wZ8?usp=sharing
https://colab.research.google.com/drive/1MSnbhCSZGqhfFrUuJWZbr-X_3ULDo92q?usp=sharing
"""

from bs4 import BeautifulSoup as bs
import requests

SOME_URL = 'https://en.wikipedia.org/wiki/Pennsylvania'

# Retrieve page
response = requests.get(SOME_URL)
# print(response.text)
# print(response.status_code)
html_str = response.text

# Parse html using bs
soup = bs(html_str, features='html.parser')

# e.g. collect all links ont he page (independent of context)
links = soup.find_all('a')
for item in links:
    print(item.prettify())
    print(item.text)
    if 'href' in item.attrs:
        print(item['href'])

# e.g. get the coordinates
geo_dec = soup.find('span', class_='geo-dec')
print(geo_dec.text)
