# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:03:21 2023

@author: User
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

url = 'https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystation'

header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
    

# =====在TDX網站去下載臺鐵各站名的資料檔案後,再轉為字典dict=====

file = 'stationName.json'

#己經有json的檔案,就直接用with open
with open(file,'r',encoding='utf-8') as f :
    data = f.read()

train_station = json.loads(data)

stations = train_station.get("Stations", []) #抓取字典中"Stations" key,去對應value，如果key不存在，就返回空列表[]。避免程式出錯,無法執行。

name_dict={}

for s in stations:
    station_id = (s.get("StationID", "")) #抓取每個車站的ID編號
    station_name = s.get("StationName", {}).get("Zh_tw", "") #抓取每個"StationName"字典，再從中取出中文站名("Zh_tw")，如果没有中文站名,返回一個空字符串,避免程式出錯,無法執行
    
    station_number = station_id+'-'+station_name # 0000-站名
    # print(station_number)

    name_dict[station_name] = station_number
# print(name_dict)    
   


#=====開始做查詢=====
train_info = name_dict #設一(name_dict)字典的變數
print('車站:',train_info.keys()) #印出每個key,就是每個車站的中文名稱
print()    
# 自行查詢搭車的站名
start_station = input('輸入欲查詢的啟程站:')

# 設定查詢的日期
query_date = input('輸入欲乘車日期(yyyy/mm/dd):')

# 設定查詢的時間範圍
start_time = input('輸入欲查詢的起始時間(hh:mm):')
# end_time = input('輸入欲查詢的終止時間(hh:mm):')

go_station_name = train_info.get(start_station)
print('=' * 50)

param = {
    '_csrf': '372b1588-336d-4a82-9302-cfbc7f909ff6',
    'rideDate': query_date,
    'station': go_station_name #注意名稱
}


data = requests.post(url, data=param, headers=header).text

soup = BeautifulSoup(data, 'html.parser')

#順行車次
print('【順行車班】')
time_forward = soup.find(id='tab1')

trs = time_forward.find_all('tr')[1:]

for row in trs:
    no = row.find('a').text
    tds = row.find_all('td')
    span = row.find_all('span')
    
    # 取得車次的發車時間
    go = tds[1].text #抓取"每個"從啟程站發車的時間
    go_time = datetime.strptime(go, '%H:%M') #轉換go字串格式為datetime格式
    
    # 檢查是否在指定時間範圍內
    # if datetime.strptime(start_time, '%H:%M') <= go_time <= datetime.strptime(end_time, '%H:%M'): #在start_time~end_time之間查詢
    if datetime.strptime(start_time, '%H:%M') <= go_time:
        
        print('車次:', no , '('+span[2].text, span[3].text, span[4].text+')')
        # print(span[2].text, span[3].text, span[4].text)
        print(start_station , '站發車時間:', go)
        print('終點站:', tds[2].text)
        print()

#逆行車次
print('【逆行車班】')
time_forward = soup.find(id='tab2')

trs = time_forward.find_all('tr')[2:]

for row in trs:
    no = row.find('a').text
    tds = row.find_all('td')
    span = row.find_all('span')
    
    # 取得車次的發車時間
    go = tds[1].text
    go_time = datetime.strptime(go, '%H:%M') #轉換go字串格式為datetime格式
    
    # 檢查是否在指定時間範圍內
    # if datetime.strptime(start_time, '%H:%M') <= go_time <= datetime.strptime(end_time, '%H:%M'): #在start_time~end_time之間查詢
    if datetime.strptime(start_time, '%H:%M') <= go_time:
        
        print('車次:', no , '('+span[2].text, span[3].text, span[4].text+')')
        # print(span[2].text, span[3].text, span[4].text)
        print(start_station , '站發車時間:', go)
        print('終點站:', tds[2].text)
        print()

#如果要查詢欲搭車的時間後的所有車班,那【end_time = input('輸入欲查詢的終止時間(hh:mm):')】就不用輸入

