def number_triangleL(n):
    if n < 2 or n > 9:
        return print("out of range")
    for i in range(1, n + 1):
        print(" " * (n- i), end = "")
        for j in range(n - i + 1, n + 1 ):
            print(j, end="")
        print()    

number_triangleL(5)
