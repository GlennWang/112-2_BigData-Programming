import numpy as np

A = np.arange(1, 10).reshape(9, 1)
B = np.arange(1, 10).reshape(1, 9)
C = np.dot(A, B)

row, col = C.shape  # 取得列行的方法。
for r in range(row):
    for c in range(col):
        print(f"{C[r, c]:2}", end=' ')
    print()