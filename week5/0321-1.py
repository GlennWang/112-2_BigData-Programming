"""
題目：1
從 |1|2|3|4|5| 到下列圖形。
請用 Python 寫一個 Bingo 遊戲的表格生成程式。
可以透過參數來指定想要生成的是: 每邊有 2 ~ 9 個數字的正方形，並依序將數字從 1 開始，隨機地填滿所有的方格。

底下是一個示範例子:
生成每邊 5 個數字的正方形，並以數值 1~25 採隨機且置中的形式，放入每一方格中。
+----+----+----+----+----+
| 19 | 12 | 21 | 17 | 16 |
+----+----+----+----+----+
| 1  | 23 | 11 | 4  | 22 |
+----+----+----+----+----+
| 15 | 25 | 7  | 13 | 6  |
+----+----+----+----+----+
| 2  | 14 | 10 | 24 | 20 |
+----+----+----+----+----+
| 8  | 5  | 18 | 9  | 3  |
+----+----+----+----+----+

請觀察上述分隔內容的橫向直線，請嘗試用字串的加法與乘法來簡要表示，不要逐字元列出。 
"""
import random

# 思路：生出數字打亂，裝進list後append進另一個list。

def generate_bingo_square(side_length):
    if side_length < 2 or side_length > 9:
        return print("out of range")
    numbers = random.sample(range(1, side_length ** 2 + 1), side_length ** 2)
    bingo_square = []
    for i in range(side_length):
        row = numbers[i * side_length: (i + 1) * side_length]
        bingo_square.append(row)

    horizontal_line = "+----" * side_length + "+"

    print(horizontal_line)
    for row in bingo_square:
        print("|" + "|".join(str(num).center(4) for num in row) + "|")
        print(horizontal_line)

generate_bingo_square(5)
