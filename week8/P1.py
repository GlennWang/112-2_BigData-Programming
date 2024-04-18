"""
題目：1
已知 lst = [k for k in range(1, 9)],
請使用 numpy 的 reshape，寫出將 lst 合法重組後所有的可能列行組合，並將重組的結果列印出來。
例如，lst = [1, 2, 3, 4, 5, 6, 7, 8] 可以重組出下列的 numpy 陣列:
1x8:
[[1 2 3 4 5 6 7 8]]
2x4:
[[1 2 3 4]
 [5 6 7 8]]
4x2:
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
8x1:
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]]
"""
import numpy as np

lst = [k for k in range(1, 9)]
size = len(lst)

ary = np.array(lst)
for r in range(1, size + 1):
    if size % r == 0:
        print(f"{r}x{size//r}:")
        print(ary.reshape(r, size//r))