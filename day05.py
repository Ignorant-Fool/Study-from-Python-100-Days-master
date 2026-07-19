"""
day05

Author:ignorant-fool
Version:0.1
Date:2026/7/19
"""
import os
from dataclasses import replace

# project30 - 定义字符串类型的变量

# s1 = 'hello,world!'
# s2 = '你好，世界！'
# print(s1)
# print(s2)

# s3 = '''I love you.
# I love my city.
# 就像你永远爱我一样.
# I know you are the rainbow of my heart.
# 就像你永远爱我一样.'''
# print(s3)

# s4 = '\141\142\143\n\x61\x62\x63'
# s5 = '\u9a86\t\u660a'                           # Unicode字符编码
# s6 = r'\u9a86\t\u660a'
# s7 = '\'hello,world\''
# print(s4)
# print(s5)
# print(s6)
# print(s7)


# project31 - 字符串相关的运算

# 拼接
# s1 = 'hello'
# s2 = 'world'
# print(s1 + ' ' + s2)

# 重复
# s3 = s1 * 10
# print(s3)

# 比较
# print(s1 < s2)
# print(s1 == 'hello')
# print(s1 > 'Hello')
# print(ord('h'))
# print(ord('H'))
# print('骆昊' < '王大锤')
# print(ord('骆'))
# print(ord('王'))

# 成员
# print('he' in s1)
# print('ok' not in s2)

# 索引
# s4 = 'I love you.'
# print(s4[0],s4[7],s4[-1])
# TypeError: 'str' object does not support item assignment
# s4[0] = 'i'

# 切片
# print(s4[2:6])
# print(s4[5:1:-1])
# print(s4[::-1])

# 遍历
# s5 = '长风破浪会有时直挂云帆济沧海'
# for i in range(len(s5)):
#     print(s5[i])
# for ch in s5:
#     print(ch)


# project32 - 字符串类型相关的操作(方法)

# 大小写
# s1 = 'hello,world!'
# print(s1.lower())                               # 每个字母小写
# print(s1.upper())                               # 每个字母大写
# print(s1.capitalize())                          # 每个单词首字母大写
# print(s1.title())                               # 第一个单词首字母大写
# print(s1)

# 性质判定
# s2 = 'abc123456'
# print(s2.isalpha())                               # 判断字符串是否全为字母
# print(s2.isdigit())                               # 判断字符串是否全为数字
# print(s2.isalnum())                               # 判断字符串是否为字母和数字组成
# print(s2.startswith('abc'))                       # 判断是否以目标字符串开头
# print(s2.endswith('123'))                         # 判断是否以目标字符串结尾

# 查找子串
# s3 = 'I love you. I love my city.'
# print(s3.index('love'))
# print(s3.index('love',5))
# ValueError: substring not found
# print(s3.index('love',15))
# print(s3.find('love',5))
# print(s3.find('love',15))                           # 找不到返回'-1'
# print(s3.rfind('love'))                             # 从右向左找到第一个目标字符串
# print(s3.rindex('love'))

# 对齐和填充
# s4, s5 ='Hello', '123'
# print(s4.center(20))
# print(s4.center(20,'~'))
# print(s4.ljust(20,'~'))
# print(s4.rjust(20,'~'))
# print(s5.zfill(5))                                  # 零填充

# 格式化
# a, b = 123, 321
# print('{0} / {1} = {2:.2%}'.format(a, b, a / b))
# print('{0} * {1} = {2:.4e}'.format(a, b, a * b))
# print(f'{a} * {b} = {a * b:.4e}')

# 修剪
# s6 = '  ~~~~hello~~~~  '
# print(s6.strip())                                     # 默认修剪空格
# print(s6.strip().lstrip('~'))
# print(s6.strip().rstrip('~'))
# print(s6.strip().strip('~'))
# print(s6.strip('~'))

# 替换
# print(s6.replace('~',''))
# print(s6.replace('~','',2))
# print(s6.replace('~','#').replace(' ',''))

# 拆分和合并
# s7 = 'ant, bird, cat, dog, eagle, fox, giraffe'
# print(s7.split())
# print(s7.split(', '))
# print(s7.split(', ',2))
# s8 = ['131','5566','7788']
# print('-'.join(s8))

# 编码和解码
# print('骆昊'.encode())
# print('骆昊'.encode('gbk'))
# print('🍎'.encode())
# print(b'\xf0\x9f\xa5\xb4'.decode())


# prject33 - 跑马灯文字

# import time

# greeting = '祝各位小伙伴在新的一年成为更好的自己' + ' ' * 15

# while True:
#     os.system('cls')
#     print(greeting)
#     greeting = greeting[1:] + greeting[0]
#     time.sleep(0.2)