# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 00:23:46 2023

@author: User
"""

from bs4 import BeautifulSoup
import requests

url = 'https://service.standardchartered.com.tw/tw/check/inquiry-rate-foreign-exchange.aspx'

header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

data = requests.get(url, headers=header).text

soup = BeautifulSoup(data, 'html.parser')

rate = soup.find(id='plExchange')

us = rate.find('tbody')

# 美元USD--因有其他不需要的資訊,因此美元的匯率另外處理
us_title = us.find('td', {'class': 'td_title show'})
print(us_title.text.strip())  # 美元(USD)

us_td = us.find('td', {'class': 'td_table_cont'})

us_tr = us_td.find_all('tr')[0:2]
# print('us_tr:',us_tr)

for row in us_tr:
    
    tds = row.text.strip().split()    
    print(tds[0])
    print(tds[1])
    print(tds[2])
    
# 其他貨幣
other_titles = us.find_all('td', {'class': 'td_title'})[1:]

for title in other_titles:
    
    span = title.find('span')
    print()
    print(span.text)  # 其他幣別

    other_td = title.find_next('td', {'class': 'td_table_cont'})
    
    other_table = other_td.find_all('tr')
    
    for row1 in other_table:
        tds1 = row1.text.strip().split()
        
        print(tds1[0])
        print(tds1[1])
        print(tds1[2])
            
            