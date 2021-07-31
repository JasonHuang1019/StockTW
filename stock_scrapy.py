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
import time
import pandas as pd


today=datetime.date.today()

year = today.year
month = today.month
day = today.day

day = 7

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.twse.com.tw/zh/page/trading/exchange/TWT93U.html")

select_year = Select(browser.find_element_by_name("yy"))
select_year.select_by_value(str(year))  # 選擇傳入的年份

select_month = Select(browser.find_element_by_name("mm"))
select_month.select_by_value(str(month))  # 選擇傳入的年份

select_day = Select(browser.find_element_by_name("dd"))
select_day.select_by_value(str(day))  # 選擇傳入的年份

time.sleep(2)
find_button = browser.find_elements_by_xpath("/html/body/div[1]/div[1]/div/div/main/div[2]/div/div/form/a")[0]
find_button.click()

time.sleep(2)
select_length = Select(browser.find_element_by_name("report-table_length"))
select_length.select_by_value("-1") 


html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

div = soup.select_one("div#report-table_wrapper")
table = pd.read_html(str(div))[0]

type(table)
table.info()
# table.dropna()
# table.drop(axis = -1)

table.sort_values([('借券賣出', '當日賣出')], ascending=False)
table.drop(columns = [('備註', '備註'),])


#%%

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