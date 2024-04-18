"""
題目：5
限使用 insert 與 append 來將逐項生成的數值([0,99])，放入串列中，並隨時維持該串列元素均為"由小到大"的排列形式。
底下是逐項生成元素，並將其插入現有串列的參考輸出結果:

value3 = [45]
value3 = [35, 45]
value3 = [7, 35, 45]
value3 = [7, 35, 45, 80]
value3 = [7, 35, 45, 74, 80]
value3 = [7, 35, 45, 74, 80, 90]
value3 = [7, 24, 35, 45, 74, 80, 90]
value3 = [0, 7, 24, 35, 45, 74, 80, 90]
value3 = [0, 7, 24, 35, 45, 50, 74, 80, 90]
value3 = [0, 7, 23, 24, 35, 45, 50, 74, 80, 90]
value3 = [0, 7, 23, 24, 35, 42, 45, 50, 74, 80, 90]
value3 = [0, 7, 9, 23, 24, 35, 42, 45, 50, 74, 80, 90]
"""
import random

number_list = []

for i in range(12):
    random_number = random.randint(0, 99)
    
    inserted = False
    for j in range(len(number_list)):
        if random_number < number_list[j]:
            number_list.insert(j, random_number)
            inserted = True
            break
    if not inserted:
        number_list.append(random_number)
    
    print(f'value3 = {number_list}')