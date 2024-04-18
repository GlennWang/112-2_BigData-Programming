"""
題目：2
請先寫一個 Triangle 類別，包含下列函式:

class Triangle:
    def __init__(self, a, b, c):  # 你可以在此判斷 a, b, c 是否可構成一個三角形。
        pass
        
    # 形成合法三角形的規則: 任兩邊和 大於 第三邊！       
    def check(self):
        return True or False 並告知是否能構成一個三角形。
        
    def area(self):  # 可以使用 Heron's formula。
        return area_value
    
    def perimeter(self):
        return perimeter_value
    
    def show(self):  # 顯示這是三角形，及三個邊長的資料。
        pass
        
最後使用下列邊長資料來逐一建構 Triangle 物件，同時將所有合法的三角形列出，並計算這些三角形的面積總和。
1) 12,  9,  6
2) 10, 10, 10
3)  6,  8, 13
4)  3, 15,  2
5) 10,  8,  4
6)  2,  4,  3
7)  3, 14,  8
8)  6, 12, 12
9) 10, 14, 13

驗證資訊: 
1)上述第 1, 2, 3, 5, 6, 8, 9 項可以構成三角形。
2)合法三角形的面積總和約為 201.5。 
"""
import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # 三角形任兩邊的和會大於第三邊
    def check(self):
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def show(self):
        print(f"This is a triangle with sides: {self.a}, {self.b}, {self.c}")

triangle_data = [
    (12, 9, 6),
    (10, 10, 10),
    (6, 8, 13),
    (3, 15, 2),
    (10, 8, 4),
    (2, 4, 3),
    (3, 14, 8),
    (6, 12, 12),
    (10, 14, 13)
]

total_area = 0
for sides in triangle_data:
    triangle = Triangle(*sides)
    if triangle.check():
        triangle.show()
        print("Area:", triangle.area())
        print("Perimeter:", triangle.perimeter())
        print("------------------------")
        total_area += triangle.area()

print("Total area of valid triangles:", total_area)
