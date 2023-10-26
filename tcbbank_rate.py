# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:46:39 2023

@author: User
"""

from bs4 import BeautifulSoup
import requests

url = 'https://rate.tcbbank.com.tw/CIB/cb5/cb501014/CB501014_01.faces'

header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

data = requests.get(url, headers=header).text
# print(data)

soup = BeautifulSoup(data, 'html.parser')

rate = soup.find('table',{'class':'tb2 m10'})
# print(rate)

ratedata = rate.find_all('tr')[1:]
# print(ratedata)
    
for row in ratedata:
    tds = row.find_all('td')
    
    #直印
    # print(tds[0].text)
    # print(tds[1].text)
    # print(tds[2].text)
    # print(tds[3].text)
    # print(tds[3].text)
    # print()
    
    #橫印
    print(tds[0].text)
    print(tds[1].text,tds[2].text,tds[3].text,tds[4].text)
    print()
    


# for row in ratedata:
#     tds = row.find_all('td',{'class':'lt'})
#     print(tds[0].text)
    
#     tds1 = row.find_all('td',{'class':'rt'})
#     print(tds1[0].text)
#     print(tds1[1].text)
#     print(tds1[2].text)
#     print(tds1[3].text)
#     print()