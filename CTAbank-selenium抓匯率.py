# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 22:58:57 2023

@author: User
"""

from bs4 import BeautifulSoup
from selenium import webdriver   # 擷取動態網頁的模組


url = "https://www.cotabank.com.tw/web/interest_3/"

header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'

    }

# 用selenium開啓瀏灠器    
openDriver = webdriver.Chrome()

# 抓取網頁
openDriver.get(url)

# 等待3秒,確保網頁載入
openDriver.implicitly_wait(3)

# 取得網頁資料
data = openDriver.page_source

# 開閉瀏灠器
openDriver.close()

# 開始解析內容
soup = BeautifulSoup(data, 'html.parser')

rate = soup.find('div', {'class':'scrollbox'})

trs = (rate.find('tbody')).find_all('tr')[2:]  # 以下兩行的合併

# 上面那行拆解如下:
# tbody = rate.find('tbody')        # 找出('div', {'class':'scrollbox'})裡的tbody的區塊
# trs = tbody.find_all('tr')[2:]    # 找出tobody裡的tr區塊,且從位置2開始找到最後

for item in trs:                    # 將找出的tr,逐一帶入變數item
    tds = item.find_all('td')       # 再從中把td再帶出來
    print(tds[0].text)              # 以下是印出位置0~4 內容,並只取文字部份
    print(tds[1].text)
    print(tds[2].text)
    print(tds[3].text)
    print(tds[4].text)

    print()



