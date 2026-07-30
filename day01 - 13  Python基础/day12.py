"""
day12

Author:ignorant-fool
Version:0.1
Date:2026/7/27
"""

# project63 - 平面上的点

# 要求：定义一个类描述平面上的点，提供计算到另一个点距离的方法。

# class Point:
#     """平面上的点"""
#
#     def __init__(self, x =0, y=0):
#         """
#         初始化方法
#         :param x: 横坐标
#         :param y: 纵坐标
#         """
#         self.x, self.y = x, y
#
#     def distance_to(self, other):
#         """
#         计算与另一个点的距离
#         :param other: 另一个点
#         """
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return (dx * dx + dy * dy) ** 0.5
#
#     def __str__(self):                                  # 当需要把对象转换成人类可读的字符串时，自动调用这个方法，返回你定义好的文本。
#         return f'({self.x}, {self.y})'
#
# p1 = Point(3,5)
# p2 = Point(6,9)
# print(p1)                                               # 调用对象的__str__魔法方法
# print(p2)
# print(p1.distance_to(p2))


# project64 - 动态属性

# class Student:
#
#     # 如果不希望在使用对象时动态的为对象添加属性，可以使用Python语言中的__slots__魔法。
#     __slots__ = ('name', 'age')
#     # 这样Student类的对象只能有name和age属性
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# stu = Student('王大锤', 20)
# # AttributeError: 'Student' object has no attribute 'sex' and no __dict__ for setting new attributes
# stu.sex = '男'                                          # 给学生对象动态添加sex属性


# project65 - 静态方法和类方法

# class Triangle(object):
#     """三角形"""
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     # @staticmethod
#     # def is_valid(a, b, c):
#     #     """判断三条边长能否构成三角形(静态方法)"""
#     #     return a + b > c and a + c > b and b + c > a
#
#     @classmethod
#     def is_valid(cls, a, b, c):
#         """判断三条边长能否构成三角形(类方法)"""
#         return a + b > c and a + c > b and b + c > a
#
#     @property                                            # property装饰器使当前方法变成属性
#     def perimeter(self):
#         """计算周长"""
#         return self.a + self.b + self.c
#
#     def area(self):
#         """计算面积"""
#         p = self.perimeter / 2
#         return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
#
# if Triangle.is_valid(3, 4, 5):
#     t = Triangle(3, 4, 5)
#     print(f'周长: {t.perimeter}')                        # 不再通过调用方法的方式来访问，而是用对象访问属性的方式直接获得
#     print(f'面积: {t.area()}')
# else:
#     print('无效的边长!!!')