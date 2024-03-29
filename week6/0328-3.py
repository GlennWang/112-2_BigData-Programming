import requests
import csv

# 下載 CSV 檔案
url = 'https://stats.moe.gov.tw/files/school/112/u1_new.csv'
response = requests.get(url)

def string_length(msg):
    total_length = 0
    for char in msg:
        if ord(char) >= 0x4E00 and ord(char) <= 0x9FFF:  # 檢查是否為中文
            total_length += 2
        else:
            total_length += 1
    return total_length

# 建立文字表格形式的學校名稱和地址
table_output = ""
if response.status_code == 200:
    # 解析CSV檔案
    csv_data = response.text.splitlines()
    csv_reader = csv.reader(csv_data)
    next(csv_reader)  # 跳過標頭
    for row in csv_reader:
        # 確保CSV檔案行數足夠長
        if len(row) >= 8:
            school_name = row[2].strip()  # 去除空白字符
            address = row[5]
            school_type = row[3]
            # 檢查地址是否包含臺北市並且是公立學校
            if "臺北市" in address and school_type == "公立":
                # 計算需要填充的空格數
                name_spaces = (22 - string_length(school_name)) // 2
                address_spaces = 36 - string_length(address)
                table_output += f"+{'-' * 22}+{'-' * 36}+\n"
                table_output += f"|{' ' * name_spaces + school_name + ' ' * name_spaces}|{address + ' ' * address_spaces}|\n"
    table_output += f"+{'-' * 22}+{'-' * 36}+\n"

# 輸出文字表格形式的結果
print(table_output)
