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

print('**************39樂合彩區塊**************')

result = soup.find('div',{'class':'contents_box03'})
# print(result)

needtime = result.find('div',{'class':'contents_mine_tx02'}).text #印出來是日期、彩券期別、開獎結果
print(needtime +':')


str_number = result.find_all('div',{'class':'ball_tx ball_lemon'})[0:5]
# print(str_number)


# str_number(str格式)轉成整數(int),為了做後面排序
int_number = [int(n.text) for n in str_number]
                #把str_number裡的數字,各別抓出,並轉成int

print('開出順序:',end='')
for n in int_number: #把轉成整數的號碼一個一個抓出來   
    print(n,end=',')
print()
print()    

#把int_number遞增排序
sorted_numbers = sorted(int_number)
# print(sorted_numbers)

print('大小順序:', end='')
for n1 in sorted_numbers: #排序完後,再一個一個抓出來
    print(n1, end=',')
print()


