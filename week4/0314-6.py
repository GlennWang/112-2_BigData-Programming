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
