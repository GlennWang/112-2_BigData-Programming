index = 9
for i in range(1, 10):
    for j in  range(1, 10):
        if (i * j < 10) and (j == 1)and j < index:
            print(f'     ', end= " ")
        elif j < index:
            print(f'      ', end= " ")
        elif (i * j < 10) and j > 1:
            print(f'{i}x{j}= {i * j}', end= " ")
        else:
            print(f'{i}x{j}={i * j}', end= " ")
    index -= 1
    print()