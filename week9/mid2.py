"""
請前往政府開放資料平台，讀取"112學年大專校院圖書館統計(校別CSV檔)"。
(https://stats.moe.gov.tw/files/detail/112/112_library2.csv)

並完成下列訊息的查找:

請問所有位在 新北市 內的國立大學，其'電子書(種)'的總和是
"""
import requests
import csv

# 下載 CSV 檔案
url = 'https://stats.moe.gov.tw/files/detail/112/112_library2.csv'
response = requests.get(url)



sum = 0
if response.status_code == 200:
    # 解析CSV檔案
    csv_data = response.text.splitlines()
    csv_reader = csv.reader(csv_data)
    next(csv_reader)  # 跳過標頭
    for row in csv_reader:
        # 確保CSV檔案行數足夠長
        if len(row) >= 27:
            # school_name = row[2].strip()  # 去除空白字符
            # address = row[5]
            cityname = row[3]
            ebook = row[18]
            school_type = row[2]

            # 檢查地址是否包含臺北市並且是公立學校
            if "新北市" in cityname and "國立" in school_type:
                print(ebook)
                sum += int(ebook)
print(f'sum:{sum}')        



