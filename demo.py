# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 22:46:40 2021

@author: Huang
"""

import requests
import pandas as pd
from matplotlib import  pyplot as plt

import mplfinance as mpf

url = "https://api.finmindtrade.com/api/v4/data"
parameter = {
    "dataset": "TaiwanStockPrice",
    "data_id": "2330",
    "start_date": "2020-01-01",
    "end_date": "2020-07-27",
    "token": "", # 參考登入，獲取金鑰
}

resp = requests.get(url, params=parameter)
data = resp.json()
data = pd.DataFrame(data["data"])
print(data.head())

plt.plot()

df = pd.DataFrame(data, columns = ['date', 'open','max','min','close','data.Trading_Volume'],)
df.set_index('date', inplace=True)

mpf.plot(df,type='candle')
