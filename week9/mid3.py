"""
題目：1
請造訪 "政府開方資料平台"，以關鍵字 "大專院校各校科系別學生數" 進行查詢。
抓回 112 學年度的資料: https://stats.moe.gov.tw/files/detail/112/112_students.csv。
請以 臺中市 內的所有大專院校為範圍:
找出該城市內所有科系名中有 "資訊" 兩個字的科系，將其依 縣市、學校名稱、系名，以及 大學部的男學生總數 與 女學生總數 列出來。
其中，大學部的定義為: 資料中屬於 "D 日"，以及"B 學士"，"B 大學" 或 "B 四技" 才算。
資料請以 HTML 表格的形式呈現出來，並以上述的欄位名稱做為抬頭列(必要時移除不需要的引號)，最後將合成資料存成 "你的學號.html"。
以 台北市 為例的參考輸出如下: 

http://114.34.49.232/~richwang/exercise/112-2/BigData/109590003-2024-0418.html
http://114.34.49.232/~richwang/Quiz-11x/112-2/BigData/109590003-2024-0418.html
"""

import requests
import csv

# 下載 CSV 檔案
url = 'https://stats.moe.gov.tw/files/detail/112/112_students.csv'
response = requests.get(url)

table_output = "<table border=\"1\">"
table_output += "\n<tr><td>縣市</td><td>學校名稱</td><td>系名</td><td>男生計</td><td>女生計</td></tr>"
if response.status_code == 200:
    csv_data = response.text.splitlines()
    csv_reader = csv.reader(csv_data)
    next(csv_reader)
    for row in csv_reader:
        if len(row) >= 28:

            # 縣市、學校名稱、系名，以及 大學部的男學生總數 與 女學生總數
            cityname = row[26]
            school_name = row[2]
            department_name = row[4]
            numofmale = row[8]
            numboffemale = row[9]
            ttt = row[5]
            ggg = row[6]

            # "D 日"，以及"B 學士"，"B 大學" 或 "B 四技"
            if "臺中市" in cityname and "資訊" in department_name and ("D 日" in ttt and ("B 學士" in ggg or "B 大學" in ggg or "B 四技" in ggg)):
                table_output += f'\n<tr><td>臺中市</td><td>{school_name}</td><td>{department_name}</td><td>{numofmale}</td><td>{numboffemale}</td></tr>'

with open('output.html', 'w', encoding='utf-8') as f:
    f.write(table_output)
