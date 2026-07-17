"""
day03

Author:ignorant-fool
Version:0.1
Date:2026/7/17
"""

# project14 - while循环

# balance = 1000
# bet_amount = 0

# while True:
#     bet_amount = int(input('请下注：'))
#     if 0 < bet_amount <= balance:
#         break

# print(f'您的下注金额为：{bet_amount}元.')


# project15 - while循环

# total = 0
# i = 1
# while i <= 100:
#     total = total + i
#     i = i + 1
# print(total)


# project16 - 猜数字小游戏

# import random

# num = random.randrange(1,100)
# counter = 0
# while True:
#     counter += 1
#     thy_num = int(input('请输入：'))
#     if thy_num < num:
#         print('大一点.')
#     elif thy_num > num:
#         print('小一点.')
#     else:
#         print('恭喜你猜对了.')
#         break

# if counter > 7:
#     print('智商余额明显不足')


# project17 - 在100-999范围内寻找水仙花数

# 一个数等于它各个位上的数字的立方和，例如：153 = 1**3 + 5**3 + 3**3
#                                      =  1   + 125  +  27

# for num in range(100,1000):
#     ones = num % 10
#     tens = num // 10 % 10
#     huns = num // 100
#     if(ones ** 3 + tens ** 3 + huns ** 3 == num):
#         print(num)


# project18 - 输出100以内的质数

# for num in range(2,100):
#     is_prime = True
#     sqrt_num = int(round(num ** 0.5,0))
#     for div in range(2,sqrt_num + 1):
#         if num % div == 0:
#             is_prime = False
#             break
#     if is_prime == True:
#         print(num,end=' ')


# project19 - 百钱百鸡问题

# 公鸡5元一只，母鸡3元一只，小鸡1元三只，欲用100元买100只鸡，
# 问公鸡、母鸡、小鸡各有多少只？

# for x in range(0,21):
#     for y in range(0,34):
#         z = 100 - x - y
#         if z % 3 == 0 and x * 5 + y * 3 + z // 3 == 100:
#             print(f'公鸡:{x},母鸡:{y},小鸡:{z}')


# project20 - 将一颗色子掷6000次，统计每种点数出现的次数

# import random

# f1 = 0
# f2 = 0
# f3 = 0
# f4 = 0
# f5 = 0
# f6 = 0
# for _ in range(6000):
#     face = random.randrange(1, 7)
#     if face == 1:
#         f1 += 1
#     elif face == 2:
#         f2 += 1
#     elif face == 3:
#         f3 += 1
#     elif face == 4:
#         f4 += 1
#     elif face == 5:
#         f5 += 1
#     else:
#         f6 += 1
# print(f'1点出现了{f1}次')
# print(f'2点出现了{f2}次')
# print(f'3点出现了{f3}次')
# print(f'4点出现了{f4}次')
# print(f'5点出现了{f5}次')
# print(f'6点出现了{f6}次')

# project21 - 容器型数据类型 - list

# 创建列表对象的字面量语法
# nums = [45,12,39,58,77,94,36]
# print(nums)
# fruits = ['banana','pitaya','waxberry','watermelon','grape']
# print(fruits)

# 创建列表对象的构造器语法
# chars = list('hello')
# print(chars)
# items = list(range(1,100))
# print(items)

# 成员运算 - 判断元素在不在列表容器中
# print(58 in nums)
# print(66 in nums)
# print('apple' in fruits)
# print('durian' not in fruits)

# 索引运算 - 操作列表容器中的某一个元素
# print(nums[1])
# print(nums[-1])
# nums[4] = 66
# print(nums)
# nums[-7] = 88
# nums[-1] = 10
# print(nums)

# 切片运算 - 从列表容器中取出一部分元素
# print(nums[1:6])
# print(nums[1:6:2])
# print(nums[6:1:-1])
# print(nums[6:1:-2])
# print(nums[:])
# print(nums[::2])
# print(nums[::-1])

# 合并
# print(nums + fruits)
# print(fruits + nums[::-1])

# 获取列表容器元素个数
# print(len(nums))
# print(len(fruits))

#循环遍历
# for i in range(len(fruits)):
#     print(fruits[i])
# for fruit in fruits:
#     print(fruit)


# project22 - 将一颗色子掷6000次，统计每个点数出现的次数

# import random

# counters = [0] * 6
# for _ in range(6000):
#     face = random.randrange(1,7)
#     counters[face - 1] += 1

# for i in range(1,7):
#     print(f'{i}点摇出了{counters[i - 1]}次.')
