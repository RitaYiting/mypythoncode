# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 00:12:13 2023

@author: User
"""

from bs4 import BeautifulSoup
import requests

url = 'https://accessibility.cathaybk.com.tw/exchange-rate-search.aspx'

header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

data = requests.get(url, headers=header).text
# print(data)

soup = BeautifulSoup(data, 'html.parser')
# print(soup)

rate = soup.find(id = 'MainContent_tab_rate_realtime')
# print(rate)

tbody = rate.find('tbody')
# print(tbody)

trs = tbody.find_all('tr')
# print(trs)

for row in trs:
    
    tds = row.find_all('td', {'class': 'td'})
    print(tds[0].text)
    print(tds[1].text)
    print(tds[2].text)
    print()
    

#寫get_text()也是可以的,與.text相同
# for row in trs:
#     # print(row)
#     tds = row.find_all('td', {'class': 'td'})
#     print(tds[0].get_text())
#     print(tds[1].get_text())
#     print(tds[2].get_text())
#     print()