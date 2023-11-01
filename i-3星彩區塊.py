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

print('**************3星彩區塊**************')

result = soup.find_all('div',{'class':'contents_box04'})
result_3star = result[0]
# print(result3)


needtime = result_3star.find('div',{'class':'contents_mine_tx02'}).text #印出來是日期、彩券期別、開獎結果
print(needtime +':')


number = result_3star.find_all('div',{'class':'ball_tx ball_purple'})
print('中獎號碼:', end='')
for n in number:
    print(n.text,end=',')
    

