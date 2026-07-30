"""
day09

Author:ignorant-fool
Version:0.1
Date:2026/7/23
"""


# project51 - 数据统计

# 假设样本数据保存一个列表中，设计计算样本数据描述性统计信息的函数。
# 描述性统计信息通常包括：算术平均值、中位数、极差（最大值和最小值的差）、方差、标准差、变异系数等。


# def ptp(data):
#     # 极差
#     return max(data) - min(data)

# def mean(data):
#     # 算术平均
#     return sum(data) / len(data)

# def median(data):
#     # 中位数
#     temp, size = sorted(data), len(data)
#     if size % 2 != 0:
#         return temp[size // 2]
#     else:
#         return temp[size // 2 - 1 : size // 2 + 1]

# def var(data,ddof=1):
#     # 方差
#     x_bar = mean(data)
#     temp = [(num - x_bar) ** 2 for num in data]
#     return sum(temp) / ddof - 1

# def std(data,ddof=1):
#     # 标准差
#     return var(data,ddof) ** 0.5

# def cv(data,ddof=1):
#     # 变异系数
#     return std(data,ddof) / mean(data)

# def describe(data):
#     """输出描述性统计信息"""
#     print(f'均值: {mean(data)}')
#     print(f'中位数: {median(data)}')
#     print(f'极差: {ptp(data)}')
#     print(f'方差: {var(data)}')
#     print(f'标准差: {std(data)}')
#     print(f'变异系数: {cv(data)}')


# project52 - 双色球随机选号

# 用函数重构之前双色球随机选号的例子(day04 - project26)，将生成随机号码和输出一组号码的功能分别封装到两个函数中，然后通过调用函数实现机选N注号码的功能。

# import random

# RED_BALLS = [i for i in range(1,34)]
# BLUE_BALLS = [i for i in range(1,17)]

# def choose():
#     # 生成一组随机号码
#     selected_balls = random.sample(RED_BALLS,6)
#     selected_balls.sort()
#     selected_balls.append(random.choice(BLUE_BALLS))
#     return selected_balls

# def display(balls):
#     # 格式化输出一组号码
#     for ball in balls[:-1]:
#         print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
#     print(f'\033[034m{balls[-1]:0>2d}\033[0m')

# n = int(input('生成几注号码：'))
# for i in range(n):
#     display(choose())


# project53 - 高阶函数(一等函数 - 函数是一等公民)

# 1.可以把函数赋值给变量
# 2.可以把函数作为函数的参数
# 3.可以把函数作为函数的返回值

# nums = [35, 92, 17, 48, 56, 33, 49, 22, 77]
# print(max(nums))

# f = max
# print(f(nums))
# f = min
# print(f(nums))
# f = sum
# print(f(nums))

# def is_big(num):
#     return num > 50

# def is_even(num):
#     return num % 2 == 0

# def foo(num):
#     return is_big(num) and is_even(num)

# def square(num):
#     return num ** 2

# def cube(num):
#     return num * num * num

# filter - 数据过滤 - 筛选元素
# map - 数据映射 - 把数据从一种形态变成另一种形态
# reduce - 数据规约 - 把很多的数据规约成唯一的结论
#       - Python 2：内置函数
#       - Python 3：from functools import reduce
# sorted - 排序 / max - 找最大 / min - 找最小 ---> key参数 - 接收一个函数提供比较大小的规则

# 这里不是调用is_big函数，而是将其传入filter函数
# filter函数内部会使用is_big函数来实现对元素的筛选
# print(list(filter(is_big,nums)))
# print(list(filter(is_even,nums)))
# Python中的匿名函数 ----> lambda函数
# lambda函数通常是一个表达式就能写清楚的函数，表达式的值就是函数的返回值(因变量)
# print(list(filter(lambda x: x % 2 == 0,nums)))
# print(list(filter(foo,nums)))
# print(list(filter(is_even,filter(is_big,nums))))
# temp = list(map(lambda x: x ** 3,filter(lambda x: x % 2 == 0,nums)))
# print(temp)