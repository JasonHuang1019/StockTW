# StockTW

透過爬蟲抓取證交所每日三大法人資料，藉由使用 Django REST framework用以網頁呈現，以及串接Line Notify，在Line上通知用戶

# Getting Started

首先，先將所需module 安裝完整， 若下方安裝無法安裝，則請手動安裝。

```bash
pip install -r requirements
```



- 進入./StockTW/stockbot/snippets/view.py
- 修改 token ，登入Line Notify (https://notify-bot.line.me/zh_TW/)，且進入個人頁面，即可看到權杖，將其貼上token即可，然後重新執行r。

![image-20210806002835352](C:\Users\dream\AppData\Roaming\Typora\typora-user-images\image-20210806002835352.png)

- 將目錄切換到 ./StockTW/stockbot 下方 ，並且執行下方指令，正確執行圖示如下，crtl+c 可退出:

```
python manage.py runserver
```

![image-20210806001141724](C:\Users\dream\AppData\Roaming\Typora\typora-user-images\image-20210806001141724.png)



- 點選進入 http://127.0.0.1:8000/stock，等待一下(5秒) ，Line群組(把Line Notify邀入群組)就會跳出通知。

![image-20210806003535181](C:\Users\dream\AppData\Roaming\Typora\typora-user-images\image-20210806003535181.png)





