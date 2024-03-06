for i in range(1, 10):
    for j in  range(1, 10):
        if (i * j < 10) and j > 1:
            print(f'{i}x{j}= {i * j}', end= " ")
        else:
            print(f'{i}x{j}={i * j}', end= " ")
    print()