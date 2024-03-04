"""
1.3.1： 模拟计算
"""

import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # !r 指以标准的表示形式显示属性
        return f"Vector({self.x!r},{self.y!r})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    # 此种方法会在16章详细介绍
    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __bool__(self):
        return bool(self.x or self.y)


a = Vector(1, 2)
b = Vector(3, 4)
print(a + b)
print(a * 3)

print(4 * a)
print(abs(b))
