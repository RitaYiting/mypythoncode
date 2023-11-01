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

print('***************大樂透區塊***************')

result = soup.find_all('div',{'class':'contents_box02'})
result3 = result[2]
# print(result3)


needtime = result3.find('div',{'class':'contents_mine_tx02'}).text #印出來是日期、彩券期別、開獎結果
print(needtime +':')


str_number = result3.find_all('div',{'class':'ball_tx ball_yellow'})[0:6]
# print(str_number)

special_number = result3.find('div',{'class':'ball_red'}).text


print('開出順序:',end='')
for n in str_number: 
    print(n.text.replace(' ',''),end=',')
print()
print()    


print('大小順序:', end='')
sort_number = result3.find_all('div',{'class':'ball_tx ball_yellow'})[6:12]
for n2 in sort_number:
    print(n2.text.replace(' ',''),end=',')
print()
print()


print('特別號:', special_number)
print()