"""
題目：2
請寫函式印出下列的結果(其中 2 <= n <= 9):
def number_triangle(n):
    ...
    
例如，呼叫 number_triangle(5) 的輸出結果如下: 
    5
   454
  34543
 2345432
123454321 
"""
def number_triangleL(n):
    if n < 2 or n > 9:
        return print("out of range")
    for i in range(1, n + 1):
        print(" " * (n- i), end = "")
        for j in range(n - i + 1, n + 1 ):
            print(j, end="")
        for j in range(n - 1, 0 + n - i,-1):
            print(j, end="")
        print()    

number_triangleL(5)
