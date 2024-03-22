import random

# 思路：生出數字打亂，裝進list後append進另一個list。

def generate_bingo_square(side_length):
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

generate_bingo_square(7)
