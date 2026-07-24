"""
day10

Author:ignorant-fool
Version:0.1
Date:2026/7/24
"""

# project54 - 偏函数

# 偏函数是指固定函数的某些参数，生成一个新的函数，这样就无需在每次调用函数时都传递相同的参数。

# import functools

# int2 = functools.partial(int, base=2)
# int8 = functools.partial(int, base=8)
# int16 = functools.partial(int, base=16)

# print(int('1001'))
# print(int2('1001'))
# print(int8('1001'))
# print(int16('1001'))


# project55 - 函数的练习

# 要求：设计一个函数实现对列表元素的排序

# 排序算法：选择排序、插入排序、冒泡排序、归并排序、快速排序、基数排序、桶排序

# 搅拌排序 - 鸡尾酒排序
# 9 2 3 4 5 6 7 8 1
# 2 3 4 5 6 7 8 1 9
# 1 2 3 4 5 6 7 8

# 函数的设计要做到无副作用
# def bubble_sort(data, gt=lambda x, y: x > y):
#     data = data[:]
#     for i in range(1, len(data)):
#         swapped = False
#         for j in range(len(data) - i):
#             if gt(data[j], data[j + 1]):
#                 swapped = True
#                 data[j], data[j + 1] = data[j + 1], data[j]
#         for j in range(len(data) - i - 1, -1, -1):
#             if gt(data[j], data[j + 1]):
#                 swapped = True
#                 data[j], data[j + 1] = data[j + 1], data[j]
#         if not swapped:
#             break
#     return data

# nums = [35, 92, 17, 48, 56, 33, 49, 22, 77]
# num = [9, 2, 3, 4, 5, 6, 7, 8, 1]
# words = ['Python', 'Java', 'Go', 'C++', 'C', 'JavaScript']

# print(bubble_sort(nums))
# print(nums)
# print(bubble_sort(words))
# print(bubble_sort(words,gt=lambda x, y: len(x) > len(y)))


# project56 - 装饰器

# 装饰器：用一个函数去装饰另一个函数或类并为其提供额外的功能(横切关注功能)。
#     - 装饰器函数的参数是一个函数，这个函数是被装饰的函数!!!
#     - 装饰器函数的返回值也是一个函数，这个函数是带有装饰功能的函数!!!

# 横切关注功能：跟正常代码的业务逻辑没有必然联系的功能。

# 语法糖 - 便捷语法(糖衣语法)

# import random
# import time

# def record_time(func):
#     def wrapper(*args, **kwargs):
#         # 在执行被装饰的函数前添加额外的功能
#         start = time.time()
#         ref_value = func(*args, **kwargs)
#         # 在执行被装饰的函数后添加额外的功能
#         end = time.time()
#         print(f'耗费时间：{end - start:.3f}秒')
#         return ref_value
#     return wrapper

# def download(filename):
#     # 下载文件
#     print(f'开始下载{filename}.')
#     time.sleep(2 + random.random() * 5)
#     print(f'{filename}下载完成.')

# @ record_time
# def upload(filename):
#     # 上传文件
#     print(f'开始上传{filename}.')
#     time.sleep(3 + random.random() * 6)
#     print(f'{filename}上传完成.')

# download = record_time(download)
# # 这里本质上是在调用wrapper函数
# download('MySQL从删库到跑路.avi')

# upload('Python从入门到住院.pdf')


# project57 - 练习：设计一个装饰器函数，如果被装饰的函数返回字符串，
# 将字符串每个单词首字母大写，如果返回其他类型则不做任何处理。

# import random

# def capitalize_every_word(func):
#     def wrapper(*args,**kwargs):
#         ret_value = func(*args,**kwargs)
#         if type(ret_value) == str:
#             ret_value = ret_value.title()
#         return ret_value
#     return wrapper

# # foo = capitalize_every_word(foo)
# @capitalize_every_word
# def foo():
#     return 'hello,world!'

# # bar = capitalize_every_word(bar)
# @capitalize_every_word
# def bar():
#     value = random.random()
#     if value < 0.3:
#         return True
#     elif value < 0.6:
#         return 1234
#     return 'i love you'

# print(foo())
# print(bar())


# project58 - 函数的递归调用 (recursion) - 一个函数可以直接或间接调用自身

# n! = n * (n - 1) * (n - 2) * ... * 2 * 1
# n! = n * (n - 1)!

# 两个要点：
#     - 1. 递归公式
#     - 2. 收敛条件 - 递归调用什么时候停下来！！！

# def fac(n: int) -> int:
#     if n == 0:
#         return 1
#     return  n * fac(n - 1)

# print(fac(5))