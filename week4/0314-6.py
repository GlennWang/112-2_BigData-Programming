"""
題目：6
首先請讀取資料檔: u1_new.csv (資料來源: 政府開放資料平台)。
為位於 臺北市 與 新北市 的所有大專院校，建立網頁連結，同時把地址寫在連結的下方。
請先觀察檔案，再根據指定的格式將內容篩選並以 HTML 形式呈現出來。
需要合成的內容與用到的欄位:
<a href='網址欄位' target=_blank>學校名稱欄位</a> <br>
地址欄位  <hr>
"""
import csv

# 讀取 CSV 檔案，並篩選出位於臺北市或新北市的大專院校
filtered_rows = []
with open('u1_new.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if '臺北市' in row['地址'] or '新北市' in row['地址']:
            filtered_rows.append(row)

# 以 HTML 格式呈現篩選後的結果
html_output = ''
for row in filtered_rows:
    html_output += f"<a href='{row['網址']}' target=_blank>{row['學校名稱']}</a> <br>\n{row['地址']}<hr>\n"

# 將結果寫入 HTML 檔案
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html_output)

print("HTML 檔案已生成。")
