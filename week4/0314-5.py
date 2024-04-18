"""
題目：5
有文字字串資料如下，
捐款的名單:
1) Godly Liu $2,500
2) Well-Born Chen $12,000
3) Ferris Wang $500
4) Maurice Lee $1,200
5) Fern Chang $3,000
6) Belinda Pai $4,500
7) Estra Tai $33,580
8) Ernestine Tong $4,200
9) Amanda Kao $25,000
10) Jesse Lin $10,000

請使用 Regular Expression 來完成下列指定的任務:
請從捐款的名單中找出所有的金額部分，並計算其總和。
"""
import re

data = """
捐款的名單:
1) Godly Liu $2,500
2) Well-Born Chen $12,000
3) Ferris Wang $500
4) Maurice Lee $1,200
5) Fern Chang $3,000
6) Belinda Pai $4,500
7) Estra Tai $33,580
8) Ernestine Tong $4,200
9) Amanda Kao $25,000
10) Jesse Lin $10,000
"""

# 使用正則表達式提取金額部分
amounts = re.findall(r'\$([\d,]+)', data)

# 將提取的金額部分轉換為整數並加總
total_amount = sum(int(amount.replace(',', '')) for amount in amounts)

print("總捐款金額為: ${}".format(total_amount))
