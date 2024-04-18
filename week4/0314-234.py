"""
題目：2
請撰寫可以實現矩陣相乘的程式

1)首先請寫一個函式:
def to_matrix(data, row, col):
	pass
	
能夠將傳入的 data 拆解成具有 row 列 col 行的二維串列。
同時也請確認資料的長度，是否剛好可以填滿整個的二維串列。
如果兩者不符合，也請顯示 "資料長度不符！"。
測試資料:
假設 data = [1, 2, 3, 4] 時，請代入 to_matrix(data, 2, 2) 會回傳如下的二維串列 A。
A = [ [1, 2],
      [3, 4] ]
"""
def to_matrix(data, row, col):
    if row * col != len(data):
        print("資料長度不符！")
        return None
    else:
        matrix = []
        for i in range(row):
            row_data = data[i*col:(i+1)*col]
            matrix.append(row_data)
        return matrix

"""
題目：3
2)請使用二維串列來儲存矩陣的內容，接著撰寫可以完成兩個矩陣合法相乘的函式。
def product(A, B):
	pass
	
其中，A 的行數必須等於 B 的列數。如果不滿足時，請顯示 "行列格式不符！"。
測試資料:
假設 A 與 B 的內容如下，請代入 product(A, B)，觀察回傳的二維陣列，是否如下所示?
A = [ [1, 2],
      [3, 4] ]	  
B = [ [2, 4, 6],
      [1, 3, 5] ]	  
矩陣乘積 AB，
AB = 
| 4	10	16 |
| 10	24	38 |

參考矩陣相乘的定義式。

題目：4
3)請使用 2) 中開發的 product(.) 函式，計算 A 的 10 次方，並印出運算後的內容，
其中，A = [ [1, 2], [-2, 1] ]。
底下是參考答案，方便核對你的乘法公式是否正確。
A**10 =
| 237	-3116 |
| 3116	237   | 
"""

def product(A, B):
    if len(A[0]) != len(B):
        print("行列格式不符！")
        return None
    else:
        result = []
        for i in range(len(A)):
            row_result = []
            for j in range(len(B[0])):
                val = 0
                for k in range(len(B)):
                    val += A[i][k] * B[k][j]
                row_result.append(val)
            result.append(row_result)
        return result

# 測試資料
# data = [1, 2, 3, 4]
# A = to_matrix(data, 2, 2)
# print("A =", A)

# B = [[2, 4, 6],
#      [1, 3, 5]]

# AB = product(A, B)
# print("AB =")
# for row in AB:
#     print("|", end=" ")
#     for val in row:
#         print(val, end="\t")
#     print("|")

# 計算 A 的 10 次方
A = [[1, 2], [-2, 1]]
result = A
for _ in range(9):
    result = product(result, A)

# 輸出結果
print("A**10 =")
for row in result:
    print("|", end=" ")
    for val in row:
        print(val, end="\t")
    print("|")