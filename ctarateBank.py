from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from selenium import webdriver


def Bankrates():
    url = "https://www.cotabank.com.tw/web/interest_3/"
    
    # 使用 Selenium 和 BeautifulSoup 來擷取匯率數據的邏輯
    openDriver = webdriver.Chrome()
    openDriver.get(url)
    openDriver.implicitly_wait(3)
    
    header = {
        'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }

    data = openDriver.page_source
    
    openDriver.close()

    soup = BeautifulSoup(data, 'html.parser')
    
    rate_div = soup.find('div', {'class':'scrollbox'})
    
    trs = (rate_div.find('tbody')).find_all('tr')[2:]

    # 解析匯率數據
    rates = []
    
    for item in trs:
        
        tds = item.find_all('td')
        
        currency = tds[0].text.strip()
        
        currency = currency.split()
        
        result = {}                
                
        result['currency'] = currency[0]        #幣別
        
        result['mbuy'] = tds[3].text.strip()    #現金買入
        
        result['msell'] = tds[4].text.strip()   #現金賣出
        
        result['realbuy'] = tds[1].text.strip() #即期買入
        
        result['realsell'] = tds[2].text.strip()#即期賣出
        
        rates.append(result)

    # 將匯率數據轉換為 JSON 格式並返回
    # return jsonify(rates)
    return rates

