"""
題目：2
請前往 政府資料開放平台，以關鍵字搜尋 "大專校院名錄"，
並請找到 "112學年大專校院名錄(CSV檔)" 的連結，透過此連結以 requests 將檔案爬取回來。
請為所有座落在 臺北市的公立大專院校，建立網頁連結，同時把地址寫在連結的下方。
請先觀察檔案，再根據指定的格式將內容篩選並以 HTML 形式呈現出來。
(* 讀入的資料並非每筆都符合格式，處理時需要進行不當資料的排除。)
需要合成的內容與用到的欄位:
<a href='網址欄位' target=_blank>學校名稱欄位</a> <br>
地址欄位 <hr>
參考輸出形式如下:
"""
import requests
import csv

# 下載 CSV 檔案
url = 'https://stats.moe.gov.tw/files/school/112/u1_new.csv'
response = requests.get(url)

# 建立HTML格式的連結和地址
html_output = ""
if response.status_code == 200:
    # 解析CSV檔案
    csv_data = response.text.splitlines()
    csv_reader = csv.reader(csv_data)
    next(csv_reader)  # 跳過標頭
    for row in csv_reader:
        # 確保CSV檔案行數足夠長
        if len(row) >= 8:
            school_name = row[2]
            address = row[5]
            school_url = row[7]
            school_type = row[3]
            # 檢查地址是否包含臺北市並且是公立學校
            if "臺北市" in address and school_type == "公立":
                html_output += f"<a href='{school_url}' target=_blank>{school_name}</a> <br>\n{address}<hr>\n"

# 將HTML內容寫入檔案
with open("taipei_public_schools.html", "w", encoding="utf-8") as file:
    file.write(html_output)

print("HTML檔案已成功生成！")
