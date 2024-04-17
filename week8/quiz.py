"""
inp = input("請輸入一個整數:")

當執行過上述程式碼後，請問下列運算哪些是正確的?
(複選) ---------------------------
 A) inp - 123 
 B) inp * '3' 
 C) inp * 3 
 D) inp - '123' 
 E) inp + '123' 
 F) inp + 123 
"""
# inp = input("請輸入一個整數:")
inp = '5'
# A = inp - 123 
# B = inp * '3' 
C = inp * 3 
# D = inp - '123' 
E = inp + '123' 
# F = inp + 123 
"""
下列的 Python 變數宣告，哪些是正確的?
(複選) ---------------------------
 A) abc_123 
 B) _else (底線else) 
 C) _2 (底線2) 
 D) 0x12 
 E) x1 
 F) y2 
 G) _ (底線) 
 H) for 
"""
abc_123 = 5
_else = 5
_2 = 5
# 0x12 = 5
x1 = 5
y2 = 5
_ = 5
# for = 5
"""
已知 msg = '0915248763'，請填入下列提問的答案:
msg[:7] = '0915248'。
msg[3:] = '5248763'。
msg[::-1] = '3678425190'。
msg[1::2] = '95473'。
"""
msg = '0915248763'
# print(f'msg[:7]:{msg[:7]}')
# print(f'msg[3:]:{msg[3:]}')
# print(f'msg[::-1]:{msg[::-1]}')
# print(f'msg[1::2]:{msg[1::2]}')
"""
Python程式在Jupyter中的副檔名是: .ipynb
。(英文請用小寫)
"""

"""
下列關於Python的描述，哪些是錯誤的？
(複選) ---------------------------
 A) 複合程式區塊是透過相同的縮排來區分。 
 B) 敘述的結尾必須加上分號(;)。 X
 C) 表示單行註解的符號是 #。 
 D) 程式大小寫是一樣的。 X
 E) Python是直譯式的程式語言。 X
"""

"""
for i in range(2, 5):
	print(i, i+1, sep=',', end="")
	
則上述程式碼執行後的輸出結果是:
"""
# for i in range(2, 5):
# 	print(i, i+1, sep=',', end="")
"""
Python中的 range(7)會生成數字序列，下列描述中那些是錯誤？
(複選) ---------------------------
 A) 序列長度是 7。 
 B) 數字序列從 0 開始。 
 C) 數字序列從 1 開始。 
 D) 數字序列包含 7。 
"""

"""
請完成下列判斷奇偶數 Python 程式片段的撰寫:

for k in range(5):
	if k % 2 0

		print(k, '是偶數！')
	

		print(k, '是奇數！')
"""
# for k in range(5):
# 	if k % 2 == 0:
# 		print(k, '是偶數！')
# 	else:
# 		print(k, '是奇數！')
"""
下列敘述何者有錯？
---------------------------
 A) True * 3 
 B) True + 1 
 C) True + False 
 D) False + 0.5 
 E) True + 'true' 
"""

"""
1 + 2**2 + 3**3 + ... + 6**6 =
"""
# print(1 + 2**2 + 3**3 + 4**4 + 5**5 + 6**6)
"""
請問 123456789**18 的計算結果，總共有幾位數:
"""
# result = 123456789 ** 18
# digit_count = len(str(result))
# print("計算結果：", result)
# print("位數：", digit_count)
"""
x^2 + xy + y^2 / sqrt(x^2 + y^2)
已知 x=3, y=5, 將其代入上述公式計算，請問計算結果的整數部分是
"""
# import math

# def expression(x, y):
#     numerator = x**2 + x*y + y**2
#     denominator = math.sqrt(x**2 + y**2)
#     result = numerator / denominator
#     return result

# # 測試表達式
# x = 3
# y = 5
# result = expression(x, y)
# print("結果：", result)