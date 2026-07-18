"""
day04

Author:ignorant-fool
Version:0.1
Date:2026/7/18
"""

# project23 - 列表容器常用操作(添加和删除元素)

# fruits = ['apple','banana','durian','pitaya']

# 追加元素到列表的末尾
# fruits.append('apple')
# fruits.append('apple')
# fruits.append('grape')
# fruits.append('pear')
# print(fruits)

# 在列表指定位置插入元素
# fruits.insert(1,'waxberry')
# fruits.insert(3,'pitaya')
# print(fruits)

# 通过索引删除元素
# fruits.pop()
# fruits.pop(1)
# fruits.pop(2)
# print(fruits)

# 指定元素进行删除
# while 'apple' in fruits:
#     fruits.remove('apple')
# ValueError:list.remove(x): x not in list
# fruits.remove('watermelon')
# print(fruits)

# 清空元素
# fruits.clear()
# print(fruits)


# project24 - 列表容器常用操作（查找、统计、排序、反转）

# fruits = ['apple','banana','waxberry','banana','durian',
#           'apple','apple','longan','durian','pitaya','pear',
#           'durian','longan','apple','waxberry','banana']

# 在列表容器中查找指定元素
# print(fruits.index('banana'))         #1
# print(fruits.index('banana',2))       #3
# print(fruits.index('banana',4))       #15
# ValueError: 'peach' is not in list
# print(fruits.index('peach'))

# 统计元素出现的次数
# print(fruits.count('apple'))            #4
# print(fruits.count('banana'))           #3
# print(fruits.count('waxberry'))         #2
# print(fruits.count('peach'))            #0

# 保留独一无二的元素
# temp = []
# for fruit in fruits:
#     if fruit not in temp:
#         temp.append(fruit)
# print(temp)

# 给列表元素排序
# temp.sort()
# print(temp)

# 将列表元素反转
# temp.reverse()
# print(temp)


# project25 - 列表生成式(推导式)

# import random

# 创建一个列表向其中添加十个1~99的随机整数
# nums = [random.randrange(1,100) for _ in range(10)]
# print(nums)

# 从上边的列表中筛选出偶数
# even_nums = [num for num in nums if num % 2 == 0]
# print(even_nums)

# 从上面的列表中筛选出大于50的偶数并计算平方根
# sqrt_nums = [num ** 0.5 for num in even_nums if num > 50]
# print(sqrt_nums)


# project26 - 双色球随机选号

# 从红色球(01-33号码)选出6个球，从蓝色球(01-16号码)选出1个球，共七个球组成一组号码，
# 例如：02 05 11 18 20 31 + 03，其中红色球按照从小到大的顺序输出，号码统一用0补齐两位。
# 要求：用程序实现机选N注随机号码的功能。

# 自行练习
# import random
# N = int(input('请输入注数：'))
# for _ in range(N):
#     red_count = 0
#     red = []
#     while red_count < 6:
#         red_count += 1
#         a = random.randrange(1,34)
#         if a not in red:
#             red.append(a)
#         red.sort()
#     blue = [random.randrange(1,17)]
#     print(red + blue)

# 参考答案
# import random
# n = int(input('机选几注：'))
# for _ in range(n):
#     selected_balls = []
#     while len(selected_balls) < 6:
#         red_ball = random.randrange(1,34)
#         if red_ball not in selected_balls:
#             selected_balls.append(red_ball)
#     selected_balls.sort()
#     blue_ball = random.randrange(1,17)
#     selected_balls.append(blue_ball)
#     for ball in selected_balls:
#         print(f'{ball:0>2d}',end=' ')                   #2d:两位整数，>:靠右对齐，0:用0补位
#     print()

# import random
# red_balls = [i for i in range(1,34)]
# blu_balls = [i for i in range(1,17)]
# n = int(input('机选几注:'))
# for _ in range(n):
#     selected_balls = random.sample(red_balls,6)        #sample:无放回随机抽样
#     selected_balls.sort()
#     for ball in selected_balls:
#         print(f'\033[31m{ball:0>2d}',end = ' ')
#     blue_ball = random.choice(blu_balls)                  #choice:抽出唯一一个元素
#     print(f'\033[34m{blue_ball:0>2d}')


# project28 - 元组的定义和运算

# 元组 - 不可变容器，不能添加或删除元素，不能对元素进行改修

# nums = (35,12,98,67,53,80,21)
# fruits = ('apple','banana','pitaya','waxberry')

# print(type(nums))
# print(type(fruits))

# print(len(nums))
# print(len(fruits))

# print(fruits[0],fruits[2],fruits[-1])
# print(nums[1:4])
# print(nums[:3])
# print(nums[3::2])
# print(nums[::-1])

# fruits[0] = 'durian'                  # 元组中的元素不能被修改

# print(nums < (35,22))
# print(55 in nums)
# print(80 in nums)
# print('peach' not in fruits)

# for fruit in fruits:
#     print(fruit,end = '\t')
# print()

# temp = nums + fruits
# print(temp)

# scores = ([95,98,92],
#           [65,72,63],
#           [85,78,90],
#           [66,77,88],
#           [97,98,99])
# print(type(scores))
# print(type(scores[0]))
# print(scores)
# # scores[0] = [100,100,100]             # 元组中的元素不能被修改
# scores[0][0] = 100
# scores[0][1] = 100
# print(scores)


# project29 - 元组的应用

# a = 11,22,33,44
# print(type(a))
# print(a)

# b, c, d, e = a
# print(f'b = {b}')
# print(f'c = {c}')
# print(f'd = {d}')
# print(f'e = {e}')

# f, g, h = a
# print(f'f = {f}')
# print(f'g = {g}')
# print(f'h = {h}')

# f, g, *h = a
# print(f'f = {f}')
# print(f'g = {g}')
# print(f'h = {h}')

# f, *g, h = a
# print(f'f = {f}')
# print(f'g = {g}')
# print(f'h = {h}')

# *f, g, h = a
# print(f'f = {f}')
# print(f'g = {g}')
# print(f'h = {h}')

# b, c = c, b
# print(f'b = {b},c = {c}')
# c, d, e = d, e, c
# print(f'c = {c},d = {d},e = {e}')