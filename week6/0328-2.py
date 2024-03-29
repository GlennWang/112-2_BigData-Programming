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
