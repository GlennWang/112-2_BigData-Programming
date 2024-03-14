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
