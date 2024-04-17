import numpy as np

lst = [k for k in range(1, 9)]
size = len(lst)

ary = np.array(lst)
for r in range(1, size + 1):
    if size % r == 0:
        print(f"{r}x{size//r}:")
        print(ary.reshape(r, size//r))