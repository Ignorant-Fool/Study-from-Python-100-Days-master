"""
day08

Author:ignorant-fool
Version:0.1
Date:2026/7/22
"""

# project47 - 番外：一起来研究一个面试题

# import time

# while True:
#     print('hello',end='',flush = True)                  # flush：每隔100ms输出一次 作用：告诉缓冲区，当把'hello'放到缓冲区时，直接清空缓冲区
#     time.sleep(0.1)


# project48 - 参数的默认值-1

# from random import randrange

# def roll_dice(n=2):                                     # 设置默认值为2
#     total = 0
#     for i in range(n):
#         total += randrange(1,7)
#     return total

# print(roll_dice())                                      # 没有设置参数时，参数为提前设置的默认值
# print(roll_dice(3))


# project49 - 参数的默认值-2

# def add(a=0, b=0, c=0):                               # 带默认值的参数必须放在不带默认值的参数之后,否则报错：SyntaxError: parameter without a default follows parameter with a default
#     return a + b + c

# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))


# project50 - 随机验证码

# 设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置。

# import random
# import string

# ALL_CHARS = string.digits + string.ascii_letters                    # string模块的digits代表0到9的数字构成的字符串'0123456789'，string模块的ascii_letters代表大小写英文字母构成的字符串'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'。

# def generat_code(*, code_len=4):
#     return ''.join(random.choices(ALL_CHARS,k=code_len))             # random模块的sample和choices函数都可以实现随机抽样，sample实现无放回抽样，这意味着抽样取出的元素是不重复的；choices实现有放回抽样，这意味着可能会重复选中某些元素。这两个函数的第一个参数代表抽样的总体，而参数k代表样本容量，需要说明的是choices函数的参数k是一个命名关键字参数，在传参时必须指定参数名。

# for _ in range(5):
#     print(generat_code())

# for _ in range(5):
#     print(generat_code(code_len=6))


# project51 - 