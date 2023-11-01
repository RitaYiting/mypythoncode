# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:14:23 2023

@author: USER
"""

import requests
import json
from datetime import datetime
import csv

url = 'https://www.thsrc.com.tw/TimeTable/Search'

header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

thrsinfo = {'南港':'NanGang','台北':'TaiPei','板橋':'BanQiao','桃園':'TaoYuan','新竹':'XinZhu','苗栗':'MiaoLi','台中':'TaiZhong','彰化':'ZhangHua','雲林':'YunLin','嘉義':'JiaYi','台南':'TaiNan','左營':'ZuoYing'}
print('車站:',thrsinfo.keys())    
    
start = input('輸入起程站:')
end = input('輸入終點站:')

#指定查詢的日期
query_date = input('輸入欲乘車日期(yyyy/mm/dd):')

#指定查詢的時間
start_time = input('輸入欲查詢的起始時間(hh:mm):')
# end_time = input('輸入欲查詢的終止時間(hh:mm):')

gostation = thrsinfo.get(start,'NanGang')

endstation = thrsinfo.get(end,'ZuoYing')

print('=' * 50)
    
param = {'SearchType': 'S',
'Lang': 'TW',
'StartStation': gostation,
'EndStation': endstation,
'OutWardSearchDate': query_date,
'OutWardSearchTime': start_time,
'ReturnSearchDate': query_date,
'ReturnSearchTime': start_time

         }

data = requests.post(url,data=param,headers=header).text

thsrc = json.loads(data)

items = thsrc['data']['DepartureTable']['TrainItem']


#寫入csv
fileName = 'thrsc.csv'

fObj = open(fileName,'w',newline = '') #newline = ''不要有空白行;如果沒有設定,會使表格多空一行

csvWrite = csv.writer(fObj)

csvWrite.writerow(['車次','發車時間',',到站時間','路程時間','停靠站']) #寫標頭


for row in items:
    
    #取得間"每個"從啟程站發車的時間    
    go_time = datetime.strptime(row['DepartureTime'],'%H:%M') #轉換row['DepartureTime']字串格式為datetime格式
    
    #1.設定啟程站的時間(go_time)是否在指定時間(start_time)的範圍後 #若設定這個方式,那就不用輸入【end_time = input('輸入欲查詢的終止時間(hh:mm):')】
    if go_time >= datetime.strptime(start_time,'%H:%M'):
        
    #2.設定啟程站的時間(go_time), 在指定結束時間(end_time)~指定開始時間(start_time)的範圍內
    # if datetime.strptime(end_time,'%H:%M') >= go_time >= datetime.strptime(start_time, '%H:%M'):
        print()
        print('車次:',row['TrainNumber'])
        print(start,'發車時間:',row['DepartureTime'])
        print(end,'到站時間:',row['DestinationTime'])
        print('路程時間:',row['Duration'])
        msg = ''
            
        items1 = row['StationInfo']
        print('停靠站:',end='')
        
        for row1 in items1:
            if row1['Show'] == True: #也可以寫 if row1['Show']: 就可以
                print(row1['StationName'],end=',')
                msg += row1['StationName'] + ','
        
        csvWrite.writerow([row['TrainNumber'],row['DepartureTime'],row['DestinationTime'],row['Duration'],msg])        
        
        print()
        
fObj.close()
        
    

