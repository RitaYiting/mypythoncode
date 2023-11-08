# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 22:37:07 2023

@author: User
"""

import db
import requests
from bs4 import BeautifulSoup
# from datetime import datetime


url = "https://news.cts.com.tw/real/index.html"
header = {
  'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
    
data = requests.get(url, headers=header)

data.encoding = 'utf-8'

data = data.text

soup = BeautifulSoup(data, 'html.parser')

content = soup.find(id = 'newslist-top')

post_date = content.find_all('div',{'class':'newstime'})
# print(post_date) 
for d in post_date:
    print(d.text)

allnews = content.find_all('a')

for row in allnews:
    
    if row.get('title') != None:
        
        title = row.get('title')
        print('標題:',title)
    
        link_url = row.get('href')
        print('連結:',link_url)
    
        post_time = row.find_all('div',{'class':'newstime'})[0:1]     
    
        for d in post_time:
            # print('發文時間:',d.text)
            post_date = str(d.text)     #日期時間要轉成str,在sql才能顯示
            print('發文時間:',post_date)

    print()
    

    sql = "select * from ctsnews where title = '{}' and platform='CTS'".format(title)
    db.cursor.execute(sql)        #在db資料表裡的資料集去執行sql的語法,不管有無資料集,都會回傳到cursor
    
    if db.cursor.rowcount == 0: #rowcount抓整個筆數 / == 0沒有東西,才可以新增
        sql = "insert into ctsnews(title,link_url,post_date,platform) values('{}','{}','{}','CTS')".format(title,link_url,post_date)
        db.cursor.execute(sql)    #在db資料表裡的資料集去執行sql的語法
        db.conn.commit()          #立即執行
        
db.conn.close()




