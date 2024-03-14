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
data = [1, 2, 3, 4]
A = to_matrix(data, 2, 2)
print("A =", A)

B = [[2, 4, 6],
     [1, 3, 5]]

AB = product(A, B)
print("AB =")
for row in AB:
    print("|", end=" ")
    for val in row:
        print(val, end="\t")
    print("|")

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