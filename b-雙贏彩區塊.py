# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 23:20:20 2023

@author: User
"""

import requests

from bs4 import BeautifulSoup

url = 'https://www.taiwanlottery.com.tw/index_new.aspx'

header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
    
data = requests.get(url, headers = header).text
# print(data)

soup = BeautifulSoup(data,'html.parser')
# print(soup)

print('***************雙贏彩區塊***************')

result = soup.find('div',{'class':'contents_box06'})
# print(result)

needtime = result.find('div',{'class':'contents_mine_tx09'}).text #印出來是日期、彩券期別、開獎結果
print(needtime +':')
print()

str_number = result.find_all('div',{'class':'ball_tx ball_blue'})[0:12]


print('開出順序:',end='')
for n in str_number: #把轉成整數的號碼一個一個抓出來   
    print(n.text.replace(' ',''),end=',')
print()    
print()


print('大小順序:', end='')
sort_number = result.find_all('div',{'class':'ball_tx ball_blue'})[12:24]
for n2 in sort_number:
    print(n2.text.replace(' ',''),end=',')

