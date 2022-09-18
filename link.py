
from headers import head

import requests, lxml
from bs4 import BeautifulSoup
import re
import pandas as pd 


def link_search (n):
    # n = input("Enter : ")
    params = {
    'q': n,           # search query
    'hl': 'en',       # language
    'num': '30'       # number of results
    }
    Headers = head()

    # df = pd.DataFrame(column = ["S.no", "link", "displayed_link", "domain_name"])

    html = requests.get('https://www.google.com/search', headers=Headers, params=params)
    soup = BeautifulSoup(html.text, 'lxml')

    # df = pd.DataFrame(["none", "none", "none", "none"], column = ["S.no", "link", "displayed_link", "domain_name"])

    link_ = []
    displayed_link_ = []
    domain_name_ = []
    # container with all needed data
    for result in soup.select('.tF2Cxc'):
        link = result.select_one('.yuRUbf a')['href']
        displayed_link = result.select_one('.TbwUpd.NJjxre').text
        domain_name = ''.join(re.findall(r'^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/?\n]+)', link))

    
        link_.append(link)
        displayed_link_.append(displayed_link)
        domain_name_.append(domain_name)
        

    df = pd.DataFrame([ link_, displayed_link_, domain_name_])
    df = df.transpose()
    df.columns =['link', 'd_link', 'site']
    return df


# print(link_search("link list"))
