# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 23:14:15 2023

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

# 去除字符串中的空格,取代為','
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
print()
print()

print('***************威力彩區塊***************')

result = soup.find('div',{'class':'contents_box02'})
# print(result)

needtime = result.find('div',{'class':'contents_mine_tx02'}).text #印出來是日期、彩券期別、開獎結果
print(needtime +':')

str_number = result.find_all('div',{'class':'ball_tx ball_green'})[0:6]

sec_number = result.find('div',{'class':'ball_red'}).text

print('開出順序:',end='')
for n in str_number: #把轉成整數的號碼一個一個抓出來   
    print(n.text.replace(' ',''),end=',')
print()    
print()

print('大小順序:', end='')
sort_number = result.find_all('div',{'class':'ball_tx ball_green'})[6:12]
for n2 in sort_number:
    print(n2.text.replace(' ',''),end=',')
print()
print()

print('第二區:'+ sec_number)
print()    

print('***************38樂合彩區塊***************')
#跟威力彩一樣,只是沒有第二區

result = soup.find('div',{'class':'contents_box02'})
# print(result)

needtime = result.find('div',{'class':'contents_mine_tx02'}).text #印出來是日期、彩券期別、開獎結果
print(needtime +':')

str_number = result.find_all('div',{'class':'ball_tx ball_green'})[0:6]

sec_number = result.find('div',{'class':'ball_red'}).text

print('開出順序:',end='')
for n in str_number: #把轉成整數的號碼一個一個抓出來   
    print(n.text.replace(' ',''),end=',')
print()    
print()


print('大小順序:', end='')
sort_number = result.find_all('div',{'class':'ball_tx ball_green'})[6:12]
for n2 in sort_number:
    print(n2.text.replace(' ',''),end=',')
print()
print()

print('***************大樂透區塊***************')

result = soup.find_all('div',{'class':'contents_box02'})
result3 = result[2]

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

print('***************49樂合彩區塊***************')

result = soup.find_all('div',{'class':'contents_box02'})
result3 = result[3]
# print(result3)


needtime = result3.find('div',{'class':'contents_mine_tx02'}).text #印出來是日期、彩券期別、開獎結果
print(needtime +':')


str_number = result3.find_all('div',{'class':'ball_tx ball_yellow'})[0:6]
# print(str_number)


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
    
print()
print()

print('**************39樂合彩區塊**************')

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
print()    
print()

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
print()    
print()

print('**************4星彩區塊**************')

result = soup.find_all('div',{'class':'contents_box04'})
result_3star = result[1]
# print(result3)


needtime = result_3star.find('div',{'class':'contents_mine_tx02'}).text #印出來是日期、彩券期別、開獎結果
print(needtime +':')


number = result_3star.find_all('div',{'class':'ball_tx ball_purple'})
print('中獎號碼:',end='')
for n in number:
    
    print(n.text,end=',')