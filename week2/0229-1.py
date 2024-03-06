import random

name_str = "駱俊翔、陳佳玲、鄭志丹、鄭淑玲、藍婉菁、李仰夫、王美華、霍秀蓉、陳建佑、林俊賢、馮惠雯"
names = name_str.split("、")

# 印表標頭
print(f"學生姓名 國文\t英文\t數學\t總分")

for name in names:
    # 生成隨機成績
    chinese_score = random.randint(0, 99)
    english_score = random.randint(0, 99)
    math_score = random.randint(0, 99)

    # 計算總分
    total_score = chinese_score + english_score + math_score

    # 輸出資料
    print(f"{name}\t {chinese_score:2}\t{english_score:2}\t{math_score:2}\t{total_score:3}")
