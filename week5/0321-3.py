"""
題目：3
請建立一個 Vector3 類別，並完成下列運算規則:
1) +, -: 向量間的加法與減法。
2) *: 與純量的乘法，其中純量可以左乘與右乘向量，將各分量乘上給定的數值。 
3) %: 表示 cross 運算或向量積，詳細計算規則請上網查閱。
4) dot(self, vec): 回傳 self 元素與 vec 的純量積或點乘積。
5) show(): 會給出向量的內容, ，其中 x, y, z 為各軸的分量。

__add__, __radd__
__sub__
__mul__, __rmul__
__mod__ (%)

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        pass
		
完成 Vector3 定義後，請使用下列資料進行接續的運算。
假設 vec_1 = Vector3(1, 2, 3)
     vec_2 = Vector3(6, 5, 4)
	 
接著請以程式算出下列各式的值:
1) vec_1 + vec_2
2) 2 * vec_1 - vec_2 * 3
3) vec_1.dot(vec_2)  =>(點乘積)
4) A = vec_1 % vec_2  =>(向量積)
   B = vec_2 % vec_1  =>(向量積)
   並請顯示上述定義的 A, B, A + B 的內容。
   
參考答案:
vec_1 + vec_2 => <7, 7, 7>
2 * vec_1 - vec_2 * 3 => <-16, -11, -6>
vec_1.product(vec_2) => 28
A, B, A + B => <-7, 14, -7>, <7, -14, 7>, <0, 0, 0>
"""
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
