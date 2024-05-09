import numpy as np
import random as rand

lst = [rand.randint(0, 20) for _ in range(0, 16)]

arr = np.array(lst)

A = arr.reshape(8, 2)
B = arr.reshape(2, 8)

result_np = np.dot(A, B)

A_mat = np.matrix(A)
B_mat = np.matrix(B)
result_mat = A_mat * B_mat

if np.array_equal(result_np, result_mat):
    print("兩者計算結果相同：")
    print(result_np)
else:
    print("兩者計算結果不同。")
