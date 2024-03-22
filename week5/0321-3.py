class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __mod__(self, other):
        return Vector3(self.y * other.z - self.z * other.y,
                       self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def show(self):
        print(f"<{self.x}, {self.y}, {self.z}>")

# 建立向量 vec_1, vec_2
vec_1 = Vector3(1, 2, 3)
vec_2 = Vector3(6, 5, 4)

# 1) 向量加法
result_1 = vec_1 + vec_2
print("vec_1 + vec_2 =>", end=" ")
result_1.show()

# 2) 向量乘法和減法
result_2 = 2 * vec_1 - vec_2 * 3
print("2 * vec_1 - vec_2 * 3 =>", end=" ")
result_2.show()

# 3) 向量點乘積
result_3 = vec_1.dot(vec_2)
print("vec_1.dot(vec_2) =>", result_3)

# 4) 向量積
A = vec_1 % vec_2
B = vec_2 % vec_1
result_4 = A + B
print("A =>", end=" ")
A.show()
print("B =>", end=" ")
B.show()
print("A + B =>", end=" ")
result_4.show()
