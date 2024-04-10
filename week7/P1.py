'''
Problem 1:
將三個任意長度串列的內容併排顯示:

1) 請隨機生成三個隨機長度的串列，同時分別將其內容以隨機產生的數值填入，產生的數值範圍為 1 ~ 99。
例如，下列是三個隨機串列的參考內容:
[28, 53, 34, 58, 5, 3, 24, 23, 32, 24], 
[21, 96, 82, 4], 
[75, 24, 94, 38, 71, 60, 27, 24]

2) 接著請將上述生成的串列內容，以下列直式且併排的格式(靠右對齊)印出:
lst_0 lst_1 lst_2 
   28    21    75 
   53    96    24 
   34    82    94 
   58     4    38 
    5          71 
    3          60 
   24          27 
   23          24 
   32             
   24

說明: 串列長度部分可以自行斟酌，重點只要讓它們不全等長，看得出內容長短不同即可。
'''
import random

# 思路:照著之前一直用的方法生三個list出來，然後找到它們之中最大的那個，找到這個的原因是因為要利用這個補齊
# 差距，這樣子就可以用迴圈直接跑，不會有超出迴圈的麻煩問題，然後就可以直接印
lst_0 = [random.randint(1, 99) for _ in range(random.randint(5, 10))]
lst_1 = [random.randint(1, 99) for _ in range(random.randint(4, 8))]
lst_2 = [random.randint(1, 99) for _ in range(random.randint(6, 12))]

max_length = max(len(lst_0), len(lst_1), len(lst_2))

lst_0.extend([''] * (max_length - len(lst_0)))
lst_1.extend([''] * (max_length - len(lst_1)))
lst_2.extend([''] * (max_length - len(lst_2)))

print(f'{"lst_0":<7} {"lst_1":<7} {"lst_2":<7}')
for i in range(max_length):
    print(f'{str(lst_0[i]):>6} {str(lst_1[i]):>6} {str(lst_2[i]):>6}')
