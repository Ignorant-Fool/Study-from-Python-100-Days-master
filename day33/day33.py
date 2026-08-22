"""
day33

Author:ignorant-fool
Version:0.1
Date:2026/8/22
"""

# project124 - 迭代器

# 迭代器是实现了迭代器协议的对象。

# class Fib(object):
#     """迭代器"""
#
#     def __init__(self, num):
#         self.num = num
#         self.a, self.b = 0, 1
#         self.idx = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idx < self.num:
#             self.idx += 1
#             self.a, self.b = self.b, self.a + self.b
#             return self.a
#         raise StopIteration
#
# a = Fib(10)
# for i in a:
#     print(i)
#
# b = Fib(5)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))          # StopIteration


# project125 - 生成器

# 生成器是语法简化版的迭代器

# def fib(num):
#     """生成器"""
#     a, b = 0, 1
#     for i in range(num):
#         a, b = b, a + b
#         yield a
#
# a = fib(10)
# for i in a:
#     print(i)
# b = fib(5)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))          # StopIteration


# project126 - 协程

# def calc_avg():
#     """流式计算平均值"""
#     total, counter = 0, 0
#     avg_value = None
#     while True:
#         value = yield avg_value
#         total, counter = total + value, counter + 1
#         avg_value = total / counter
#
# gen = calc_avg()
# print(next(gen))
# print(gen.send(10))
# print(gen.send(20))
# print(gen.send(30))