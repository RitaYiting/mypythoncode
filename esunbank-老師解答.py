# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:24:39 2023

@author: User
"""

from bs4 import BeautifulSoup
import requests

url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'

header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

data = requests.get(url, headers=header).text

soup = BeautifulSoup(data, 'html.parser')

rate = soup.find(id='exchangeRate')

tbody = rate.find('tbody')
# print(tbody)

trs = tbody.find_all('tr')[1:]
# print(trs)

for row in trs:

   tds = row.find_all('td',recursive = False)  #recursive = False 不做遞迴(內迴圈)-->不再往內抓 預設是True
   
   if len(tds) == 4:       
       print(tds[0].text.strip().split()[0]) #split()-->切割 [0]-->抓索引值0
       print(tds[1].text.strip())
       print(tds[2].text.strip())
       print(tds[3].text.strip())
       print()