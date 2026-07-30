"""
day07

Author:ignorant-fool
Version:0.1
Date:2026/7/21
"""

# project41 - 输入m和n,计算组合数C(m,n)的值

# def fac(num):
#     result = 1
#     for i in range(1,num + 1):
#         result *= i
#     return result

# from math import factorial as fac

# m = int(input('m = '))
# n = int(input('n = '))

# 计算C(m,n)的值
# print(fac(m) // fac(n) // fac(m - n))

# from math import comb

# print(comb(m,n))


# project42 - 设计函数的练习-1

# 需求:输出100以内的质数(只能被1和自身整除的数)

# def is_prime(num: int) -> bool:
#     for i in range(2,int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# for n in range(2,100):
#     if is_prime(n):
#         print(n)


# project43 - 设计函数的练习-2

# 求两个正整数的最大公约数和最小公倍数

# def gcd(x: int, y: int) -> int:
#     while x % y != 0:
#         x, y = y, x % y
#     return y

# def lcm(x: int, y: int) -> int:
#     return x * y // gcd(x, y)

# print(gcd(15,27))
# print(lcm(27,15))


# project44 - 函数的参数-1

# 输入三角形三条边的长度，如果可以构成三角形就计算出周长和面积。

# import math

# def judge(a, b, c, /):                                        # /强制位置参数：传参的时候必须对号入座
#     # 判断三条边能否构成三角形
#     return a + b > c and b + c > a and a + c > b

# def perimeter(a, b, c):
#     # 计算周长
#     return a + b + c

# def area(*, a, b, c):                                         # *命名关键字参数：传参的时候必须带上参数名
#     # 计算面积
#     h = perimeter(a, b, c) / 2
#     return math.sqrt(h * (h - a) * (h - b) * (h - c))

# x, y, z = map(float,input('请输入三条边的长度：').split())
# if judge(x, y, z):
#     print(f'周长：{perimeter(x, y, z)}')
#     print(f'面积：{area(x, y, z)}')


# project45 - 函数的参数-2

# 大家猜一猜Python内置函数max是如何设计的？

# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组

# 参数列表中的**kwargs可以接收0个或任意多个关键字参数
# 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
# 如果一个关键字参数都没有传入，那么kwargs会是一个空字典

# def foo(*args, **kwargs):
#     print(args)
#     print(kwargs)

# foo()
# foo(1)
# foo(1, 2)
# foo(1, 2, 3, a = 4, b = 5)
# foo(1, 2, 3, 4, 5, 6, 7, 8)
# foo([1, 2, 3, 4, 5, 6, 7, 8])
# foo([1, 2, 3, 4, 5], {6, 7, 8})


# project46 - 将1.025输出成1.03

# 在计算机中，表示小数是用有限的集合去映射无限的集合，因此一定会存在运算精度的问题

# print(0.1 + 0.2)
# print(0.1 + 0.2 + 0.3)
# print(0.3 + 0.2 + 0.1)
# print(0.1 + 0.2 + 0.3 == 0.3 + 0.2 + 0.1)

# round做的是四舍六入，五的话看前边是奇数还是偶数，银行家舍入算法
# print(f'{1.025:.2f}')
# print(round(1.025,2))
# print(f'{1.024:.2f}')
# print(round(1.024,2))
# print(f'{1.026:.2f}')
# print(round(1.026,2))