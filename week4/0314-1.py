"""
題目：1
請分別使用 random 函式庫中的 randint(0, 99) 與 gauss(70, 15) (其中，mu=70, sigma=15) 來生成 50 名學生的成績資料。
接著統計該成績的分佈區間，並將分佈的結果以下列文字的圖形形式顯示出來。
參考輸出:(你生成的內容會不一樣，但輸出時請完全仿照下列的格式。)
By randint(0, 99):
 0~ 9:******
10~19:*******
20~29:********
30~39:****
40~49:*******
50~59:****
60~69:******
70~79:*******
80~89:*****
90~99:******
------------------------
By gauss(70, 15):
 0~ 9:
10~19:
20~29:
30~39:**
40~49:********
50~59:****
60~69:**************
70~79:****************
80~89:************
90~99:****
"""
import random

# 使用 randint(0, 99) 生成 50 名學生的成績資料
randint_grades = [random.randint(0, 99) for _ in range(50)]

# 使用 gauss(70, 15) 生成 50 名學生的成績資料
gauss_grades = [int(random.gauss(70, 15)) for _ in range(50)]

# 定義函數統計成績分佈
def count_distribution(grades):
    distribution = [0] * 10
    for grade in grades:
        index = min(grade // 10, 9)
        distribution[index] += 1
    return distribution

# 定義函數輸出成績分佈圖形
def print_distribution(distribution, method):
    print(f"By {method}:")
    for i, count in enumerate(distribution):
        lower_bound = i * 10
        upper_bound = (i + 1) * 10 - 1
        print(f"{lower_bound:2}~{upper_bound:2}:", "*" * count)
    print("------------------------")

# 統計並輸出 randint(0, 99) 的成績分佈
randint_distribution = count_distribution(randint_grades)
print_distribution(randint_distribution, "randint(0, 99)")

# 統計並輸出 gauss(70, 15) 的成績分佈
gauss_distribution = count_distribution(gauss_grades)
print_distribution(gauss_distribution, "gauss(70, 15)")
