# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 15:49:43 2021

@author: Jason
"""

from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time
import pandas as pd
import dataframe_image as dfi
import os 

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless") #無頭模式
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

def total():
    today=datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
        
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://www.twse.com.tw/zh/page/trading/fund/BFI82U.html")
    
    select_year = Select(browser.find_element_by_name("yy"))
    select_year.select_by_value(str(year))  # 選擇傳入的年份
    
    select_month = Select(browser.find_element_by_name("mm"))
    select_month.select_by_value(str(month))  # 選擇傳入的年份
    
    select_day = Select(browser.find_element_by_name("dd"))
    select_day.select_by_value(str(day))  # 選擇傳入的年份
    

    find_button = browser.find_elements_by_xpath("/html/body/div[1]/div[1]/div/div/main/div[2]/div[1]/div/form/table/tbody/tr[4]/td[2]/a")[0]
    find_button.click()
    
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html,'html.parser')

    div = soup.select_one("div#report-table_wrapper")
    table = pd.read_html(str(div))[0]


    type(table)
    table.info()
    
    table.買進金額 = table.買進金額.div(100000000)
    table.賣出金額 = table.賣出金額.div(100000000)
    table.買賣差額 = table.買賣差額.div(100000000)
    
    title =  str(year-1911)+'年'+str(month)+'月'+str(day)+'日  三大法人買賣金額統計表'
    
    browser.close()
    dfi.export(table, 'table.png')
    return title, table 
    
# title, table = total()