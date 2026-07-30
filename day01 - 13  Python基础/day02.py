"""
day02

Author:ignorant-fool
Version:0.1
Date:2026/7/12
"""

# project09 - BMI(体质指数)计算器

# height = float(input('身高(cm):'))
# weight = float(input('体重(kg):'))
# bmi = weight / (height / 100) ** 2
# print(f'{bmi = :.1f}')

# if bmi < 18.5:
#     print('你的体重过轻！')
# elif bmi < 24:
#     print('你的身材很棒！')
# elif bmi < 27:
#     print('你的体重过重！')
# elif bmi < 30:
#     print('你已轻度肥胖！')
# elif bmi < 35:
#     print('你已中度肥胖！')
# else:
#     print('你已重度肥胖！')


# project10 - 输入三角形三条边的长度，如果可以构成三角形就计算周长和面积，否则提示无法构成三角形。

# import math

# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))

# if a + b > c and b + c > a and a + c > b:
#     p = a + b + c
#     h = p / 2
#     s = math.sqrt(h * (h - a) * (h - b) * (h - c))
#     print(f'周长:{p}')
#     print(f'面积:{s}')
# else:
#     print('不能构成三角形')


# project11 - for循环入门

# import time

# for i in range(0,3600):
#     if i % 2 == 0:
#         print('hello,world!')
#     else:
#         print('goodbye,world!')
#     time.sleep(1)


# project12 - 1-100的整数求和

# total = 0

# for i in range(1,101):
#     total += i

# print(total)

# print(sum(range(1,101)))


# project13 - 输出九九表

# for i in range(1,10):
#     for j in range(1,i + 1):
#         print(f'{i} * {j} = {j * i}',end = '\t')
#     print()
