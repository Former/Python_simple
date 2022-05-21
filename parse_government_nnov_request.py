# -*- coding: utf-8 -*-

# Copyright © 2022 Alexei Bezborodov. Contacts: <AlexeiBv+gov_nnov_py@narod.ru>
# License: Public domain: http://unlicense.org/

from bs4 import BeautifulSoup
import requests

base_url = "https://government-nnov.ru/"
url = base_url + "events/interview"
request = requests.get(url, verify = False)

soup = BeautifulSoup(request.text, "html.parser")

tiles = soup.find("div", class_ = "tiles tile-list")
articles = tiles.find_all("dl")
for article in articles:
    ref = article.find("a")
    if ref != None:
        print(ref['href'])
