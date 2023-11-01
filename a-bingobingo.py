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

print('***************BINGO BINGO**************')

result = soup.find('div',{'class':'contents_box01'})
# print(result)

needtime = result.find('span',{'class':'font_black15'}).text #印出來是日期、彩券期別
 
end = result.find('a').text #印出來是開獎結果
print(needtime + end +':')

# 把str格式的開出獎號轉為int整數整式  # 並去除字符串中的空格,取代為','
bingo_number = result.find('div',{'class':'ball_box01'}).text.replace(' ',',')
print('開出獎號:'+bingo_number) 
print()

super_number = result.find('div',class_='ball_red').text.strip()
print('超級獎號:', super_number)
print()

super_number1 = result.find('div',class_='ball_blue_BB1').text.strip()
print('猜大小:', super_number1)
print()

super_number2 = result.find('div',class_='ball_blue_BB2').text.strip()
print('猜單雙:', super_number2)
print()

