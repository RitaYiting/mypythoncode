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

print('**************今彩539區塊**************')

result = soup.find('div',{'class':'contents_box03'})
# print(result)

needtime = result.find('div',{'class':'contents_mine_tx02'}).text #印出來是日期、彩券期別、開獎結果
print(needtime +':')


str_number = result.find_all('div',{'class':'ball_tx ball_lemon'})[0:5]
# print(str_number)


print('開出順序:',end='')
for n in str_number: 
    print(n.text.replace(' ',''),end=',')
print()
print()    


print('大小順序:', end='')
sort_number = result.find_all('div',{'class':'ball_tx ball_lemon'})[5:10]
for n2 in sort_number:
    print(n2.text.replace(' ',''),end=',')
