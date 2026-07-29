"""
day14

Author:ignorant-fool
Version:0.1
Date:2026/7/29
"""

# project69 - 读写文本文件

# file = open('致橡树.txt','r',encoding='utf-8')
# print(file.read())
# file.close()

# 除了使用文件对象的read方法读取文件之外，还可以使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中。

# file = open('致橡树.txt','r',encoding='utf-8')
# for line in file:
#     print(line,end='')
# file.close()

# file = open('致橡树.txt','r',encoding='utf-8')
# lines = file.readlines()
# for line in lines:
#     print(line,end='')
# file.close()

# 如果要向文件中写入内容，可以在打开文件时使用w或者a作为操作模式，前者会截断之前的文本内容写入新的内容，后者是在原来内容的尾部追加新的内容。

# file = open('致橡树.txt','a',encoding='utf-8')
# file.write('\n标题：《致橡树》')
# file.write('\n作者：舒婷')
# file.write('\n时间：1977年3月')
# file.close()


# project70 - 异常处理机制

# 为了让代码具有健壮性和容错性，我们可以使用 Python 的异常机制对可能在运行时发生状况的代码进行适当的处理。
# try except else finally raise

# file = None
# try:
#     file = open('致橡树.txt','r',encoding='utf-8')
#     print(file.read())
# except FileNotFoundError:
#     print('无法打开指定的文件！')
# except LookupError:
#     print('指定了未知的编码！')
# except UnicodeDecodeError:
#     print('读取文件时解码错误！')
# else:
#     print('我使用了else')
# finally:
#     print('我使用了finally')
#     if file:
#         file.close()

# class InputError(ValueError):
#     """自定义异常类型"""
#     pass
#
# def fac(num):
#     """求阶乘"""
#     if num < 1:
#         raise InputError('只能计算非负整数的阶乘')
#     if num == 1:
#         return 1
#     return num * fac(num - 1)
#
# flag = True
# while flag:
#     num = int(input('n = '))
#     try:
#         print(f'{num}! = {fac(num)}')
#         flag = False
#     except InputError as err:
#         print(err)


# project71 - 上下文管理器语法

# 可以使用with上下文管理器语法在文件操作完成后自动执行文件对象的close方法
# 只有符合上下文管理器协议（有__enter__和__exit__魔术方法）和Python 标准库中的contextlib模块的对象才能使用这种语法。

# try:
#     with open('致橡树.txt','r',encoding='utf-8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('无法打开指定的文件！')
# except LookupError:
#     print('指定了未知的编码！')
# except UnicodeDecodeError:
#     print('读取文件时解码错误！')


# project72 - 读写二进制文件

# try:
#     with open('头像.jpg','rb') as file1:
#         data = file1.read()
#     with open('测试.jpg','wb') as file2:
#         file2.write(data)
# except FileNotFoundError:
#     print('指定的文件无法打开.')
# except IOError:
#     print('读写文件时出现错误.')
# print('程序执行结束.')

# 如果要复制的图片文件很大，一次将文件内容直接读入内存中可能会造成非常大的内存开销。
# 为了减少对内存的占用，可以为read方法传入size参数来指定每次读取的字节数，通过循环读取和写入的方式来完成上面的操作，
# try:
#     with open('头像.jpg','rb') as file1, open('测试.jpg','wb') as file2:
#         data = file1.read(512)
#         while data:
#             file2.write(data)
#             data = file1.read(512)
# except FileNotFoundError:
#     print('指定文件无法打开.')
# except IOError:
#     print('读写文件时出现错误.')
# print('程序执行结束.')


# project73 - 读写JSON格式的数据

import json

# my_dict = {
#     'name': '骆昊',
#     'age': 40,
#     'friends': ['王大锤', '白元芳'],
#     'cars': [
#         {'brand': 'BMW', 'max_speed': 240},
#         {'brand': 'Audi', 'max_speed': 280},
#         {'brand': 'Benz', 'max_speed': 280}
#     ]
# }
#
# print(json.dumps(my_dict))

# 如果要将字典处理成 JSON 格式并写入文本文件，只需要将dumps函数换成dump函数并传入文件对象即可
# with open('data.json','w') as file:
#     json.dump(my_dict, file)

# json模块有四个比较重要的函数，分别是：
# dump - 将 Python 对象按照 JSON 格式序列化到文件中
# dumps - 将 Python 对象处理成 JSON 格式的字符串
# load - 将文件中的 JSON 数据反序列化成对象
# loads - 将字符串的内容反序列化成 Python 对象

# with open('data.json','r') as file:
#     my_dict = json.load(file)
#     print(type(my_dict))
#     print(my_dict)