# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 00:40:58 2021

@author: Huang
"""

from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

import datetime
today=datetime.date.today()
print(today)

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.twse.com.tw/zh/page/trading/exchange/TWT93U.html")

select_year = Select(browser.find_element_by_name("yy"))
select_year.select_by_value((108))  # 選擇傳入的年份

select_year = Select(browser.find_elemet_by_name("report-table_length"))
select_year.select_by_value("-1") 
 
response = requests.get("https://www.twse.com.tw/zh/page/trading/exchange/TWT93U.html")
soup = BeautifulSoup(response.text, "html.parser")
 
price = soup.find("span", {"class": "price-text__current"}).getText()[7:]  #取得文字中的價格部分
 
if int(price) < 500:  #將爬取的價格字串轉型為整數
    headers = {
        "Authorization": "Bearer " + "你的權杖(token)",
        "Content-Type": "application/x-www-form-urlencoded"
    }
 
    params = {"message": "Python基礎課程和網路爬蟲入門實戰 已降價至" + price + "元"}
 
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
    print(r.status_code)  #200