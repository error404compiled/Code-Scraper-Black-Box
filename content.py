from link import link_search
from headers import head

import requests, lxml
from bs4 import BeautifulSoup
import re
import pandas as pd 

Headers = head()

def link(n):
    link = ""
    df = link_search(n)
    for i in df['link']:
        if "geeks" in i:
            link = i
            break
    # print(link)
    return link

def code (n, l):
    url  = link(n)
    html = requests.get(url, headers=Headers)
    soup = BeautifulSoup(html.text, 'lxml')
    for i in soup.select('.code')[int(l)]:
        # print(i)
        for j in i.find_all('code'):
            # print(j)
            # print("-------------------------------")
            k = j.text.rstrip()
            print(k)
            # if "�" in k:
            #     pass
            # else:   
            #     print(k)
            




