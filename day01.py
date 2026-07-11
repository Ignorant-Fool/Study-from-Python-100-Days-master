"""
day01

Author:ignorant-fool
Version:0.1
Date:2026/7/11
"""
from pandas.core.computation.engines import PythonEngine

# project01 - 注释

# 使用print函数输出字符串中的内容
# end参数可以修改输出的结束符
# print('hello,world',end = '')
# print('你好，世界！')


# project02 - 数据类型

# print(100)
# print(0b100) #二进制整数
# print(0o100) #八进制整数
# print(0x100) #十六进制整数

# print(123.456)    #浮点小数(科学写法)
# print(1.23456e2)  #浮点小数(科学计数法)

# print('hello,world') #字符串
# print("hello,world") #字符串

# print(True)  #布尔值“真”
# print(False) #布尔值“假”


# project03 - 变量的定义和使用

# 命名规则：
# 规则1 变量名由字母、数字和下划线构成，数字不能开头。
# 规则2 Python 是大小写敏感的编程语言。
# 规则3 变量名不要跟 Python 的关键字重名，尽可能避开 Python 的保留字。

# a = 45  #定义变量a，赋值45
# b = 12  #定义变量b，赋值12
# print(a + b)   #57
# print(a - b)   #33
# print(a * b)   #540
# print(a / b)   #3.75


# project04 - 使用type函数检查变量的类型

# a = 100
# b = 123.45
# c = '123.45'
# d = True
# print(type(a))  #<class 'int'>
# print(type(b))  #<class 'float'>
# print(type(c))  #<class 'str'>
# print(type(d))  #<class 'bool'>

# print(str(a))        # '100'
# print(float(c))      # 123.45
# print(int(d))        # 1
# print(int(False))    # 0

# print(ord('坤'))
# print(chr(22372))


# project05 - 算数运算符

# print(321 + 12)    #加法运算，输出333
# print(321 - 12)    #减法运算，输出309
# print(321 * 12)    #乘法运算，输出3852
# print(321 / 12)    #除法运算，输出26.75
# print(321 // 12)   #整除运算，输出26
# print(321 % 12)    #求模运算，输出9
# print(321 ** 12)   #求幂运算，输出1196906950228928915420617322241

# print(2 + 3 * 5)            # 17
# print((2 + 3) * 5)          # 25
# print((2 + 3) * 5 ** 2)     # 125
# print(((2 + 3) * 5) ** 2)   # 625


# project06 - 赋值运算符

# a = 10
# b = 3
# a += b               #相当于: a = a + b
# a *= a + 2           #相当于: a = a * (a + 2)
# print(a)


# project07 - 比较运算符和逻辑运算符

# flag0 = 1 == 1              # True
# flag1 = 3 > 2               # True
# flag2 = 2 < 1               # False
# flag3 = flag1 and flag2     # False
# flag4 = flag1 or flag2      # True
# flag5 = not flag0           # False

# print('flag0 =',flag0)      # flag0 = True
# print('flag1 =',flag1)      # flag1 = True
# print('flag2 =',flag2)      # flag2 = False
# print('flag3 =',flag3)      # flag3 = False
# print('flag4 =',flag4)      # flag4 = True
# print('flag5 =',flag5)      # flag5 = False
# print(flag1 and not flag2)  # True
# print(1 > 2 or 2 == 3)      # False


# project08 - 输入圆的半径，计算周长和面积

# r = float(input('请输入圆的半径：'))
# p = 2 * 3.1416 * r
# s = 3.1416 * r ** 2
# print(f'周长：{p:.2f}')
# print(f'面积：{s:.2f}')

