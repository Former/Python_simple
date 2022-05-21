# -*- coding: utf-8 -*-

# Copyright © 2022 Alexei Bezborodov. Contacts: <AlexeiBv+gov_nnov_py@narod.ru>
# License: Public domain: http://unlicense.org/

from bs4 import BeautifulSoup
from urllib2 import urlopen
import ssl

#import os; import locale;  os.environ["PYTHONIOENCODING"] = "utf-8";  myLocale=locale.setlocale(category=locale.LC_ALL, locale="ru_RU.UTF-8");

base_url = "https://government-nnov.ru/"
url = base_url + "events/interview"

context_ssl = ssl._create_unverified_context()
html_gover_doc = urlopen(url, context=context_ssl).read()

soup = BeautifulSoup(html_gover_doc, "html.parser", from_encoding="utf-8")

titles = soup.find("div", class_ = "tiles tile-list")
articles = titles.find_all("dl")
num_art = 0
for article in articles:
    num_art += 1
    ref = article.find("a")
    if ref != None:        
        #print(base_url + ref['href'])
        art_url = base_url + ref['href']
        html_art_doc = urlopen(art_url, context=context_ssl).read()
        soup_article = BeautifulSoup(html_art_doc, "html.parser", from_encoding="utf-8")
        content = soup_article.find("div", class_ = "content")
        
        header = content.find("h1", class_="h1-reduced");
        lead = content.find("p", class_="lead");
        
        print(num_art, ":")
        print(header.string.encode('utf-8', errors='ignore'))
        print()
        print(num_art, ":")
        print(lead.string.encode('utf-8', errors='ignore'))
        print('----------------------------------------------')
