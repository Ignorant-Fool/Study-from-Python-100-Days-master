"""
day11

Author:ignorant-fool
Version:0.1
Date:2026/7/25
"""

# project59 - 函数的递归调用 - 斐波那契数列(兔子数列、黄金分割数列)

# 1 1 2 3 5 8 13 21 34 55 ...

# f(n) = f(n - 1) + f(n + 2)

# 空间换时间 - 时间和空间是不可调和的矛盾！！！
# LRU - 缓存置换策略 - 最近最少使用(Least Recently Used)
# @lru_cache可以将之前算过的结果缓存起来，减少重复运算

# 经典问题：
# 1.汉诺塔
# 2.骑士周游
# 3.八皇后
# 4.爬楼梯

# from functools import lru_cache

# @lru_cache(maxsize=3)
# def fib(n):
#     if n in {1, 2}:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# def main():
#     for n in range(1,121):
#         print(n,fib(n))

# if __name__ == '__main__':
#     main()


# project60 - 面向对象编程 - 把数据和操作数据的函数封装成一个逻辑上的整体

# # 程序是指令的集合 ---> 指令式编程 ---> 适合解决简单的问题
# # 面向对象编程 ----> 通过给对象发消息达成解决问题的目标 ----> 适合解决复杂问题
#
# # 对象(object):接收消息的实体，一切皆为对象，具体概念。
# # 类(class):对象的蓝图和模板，把拥有共同特征的对象的特征提取出来就形成了类，抽象的概念。
# #      - 静态特征 ----> 属性
# #      - 动态特征 ----> 方法(行为)
#
# # 有了类才能创建出一个个具体的对象
#
# # 1.定义类：2.创建对象；3.给对象发消息
#
# # 1.定义类
# class Student:
#     # 1.数据抽象 ---> 属性 ---> 和对象相关的数据
#     # 特殊用法的魔术方法(magic method)
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#     # 2.行为抽象 ---> 方法 ---> 对象可接收的消息
#     def eat(self):
#         print(f'{self.name}学生正在吃饭.')
#
#     def study(self, course_name):
#         print(f'{self.name}学生正在学习{course_name}.')
#
# # 2.创建对象(构造器语法)
# stu1 = Student('骆昊',True)
# stu2 = Student('沈妙',False)
#
# # 3.给对象发消息
# stu1.eat()
# stu1.study('Python程序设计')
#
# stu2.study('数据库和SQL')
# stu2.eat()


# # project61 - 写一个类描述数字时钟
#
# # 数据抽象 - 属性 - 时、分、秒
# # 行为抽象 - 行为 - 走字、显示时间
#
# from datetime import datetime
# import time
#
# class Clock:
#     """时钟类"""
#
#     @classmethod
#     def current(cls):
#         dt = datetime.now()
#         return cls(dt.hour, dt.minute, dt.second)
#
#     def __init__(self, hour=0, minute=0, second=0):
#         """
#         初始化方法
#         :param hour: 时
#         :param minute: 分
#         :param second: 秒
#         """
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     def show(self, is_full=True):
#         """
#         显示时间
#         :param is_full: 是否使用24小时制式(默认值为True)
#         :return: 当前时间对应的字符串
#         """
#         if is_full:
#             return f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}'
#         else:
#             hour, suffix = self.hour, 'AM'
#             if hour >= 12:
#                 suffix = 'PM'
#             if hour > 12:
#                 hour -= 12
#             return f'{hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d} {suffix}'
#
#     def run(self):
#         """走字"""
#         self.second += 1
#         if self.second == 60:
#             self.second = 0
#             self.minute += 1
#             if self.minute ==60:
#                 self.minute = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0
#
# x = Clock(23,59,57)
# x = Clock.current()
# while True:
#     print(x.show())
#     x.run()
#     time.sleep(1)


# project62 - 扑克游戏

# # 牌 - 属性？？？行为？？？
# # 扑克
# # 玩家
#
# # 对象的属性：天然属性(原生属性)、计算属性
#
# import random
#
# class Card:
#     """牌"""
#
#     def __init__(self,suite, face):
#         self.suite = suite
#         self.face = face
#
#     def __repr__(self):
#         return self.show()
#
#     # less than
#     def __lt__(self, other):
#         if self.suite == other.suite:
#             return self.face < other.face
#         return self.suite < other.suite
#
#     def show(self):
#         suites = {'S': '♠️', 'H': '❤️', 'C': '♣️', 'D': '♦️'}
#         faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#         return f'{suites[self.suite]}{faces[self.face]}'
#
# class Poker:
#     """扑克"""
#
#     def __init__(self):
#         self.cards = [Card(suite, face)
#                       for suite in 'SHCD'
#                       for face in range(1,14)]
#         self.index = 0
#
#     def shuffle(self):
#         """洗牌"""
#         random.shuffle(self.cards)
#         self.index = 0
#
#     def deal(self):
#         """发牌"""
#         card = self.cards[self.index]
#         self.index += 1
#         return card
#
#     @property                                   # 属性装饰器：把方法变成属性
#     def has_more(self):
#         """判断有没有牌可以发出"""
#         return self.index < len(self.cards)
#
# class Player:
#     """玩家"""
#
#     def __init__(self, nickname):
#         self.nickname = nickname
#         self.cards = []
#
#     def get_more(self, card):
#         """摸牌"""
#         self.cards.append(card)
#
#     def arrange(self):
#         """整理手上的牌"""
#         self.cards.sort()
#
# def main():
#     poker = Poker()
#     poker.shuffle()
#
#     players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
#
#     for _ in range(13):
#         for player in players:
#             card = poker.deal()
#             player.get_more(card)
#
#     for player in players:
#         player.arrange()
#         print(player.nickname,end = ':')
#         print(player.cards)
#
#
#
# if __name__ == '__main__':
#     main()