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
