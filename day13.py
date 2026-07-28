"""
day13

Author:ignorant-fool
Version:0.1
Date:2026/7/28
"""

# project66 - 继承和多态

# class Person:
#     """人"""
#
#     def __init__(self, name, age):
#         self.name = name
#         self.sge = age
#
#     def eat(self):
#         print(f'{self.name}正在吃饭.')
#
#     def sleep(self):
#         print(f'{self.name}正在睡觉.')
#
#
# class Student(Person):
#     """学生"""
#
#     """
#     如果不需要新加属性，可以不用写 __init__ 方法，自动继承父类的初始化。
#     ~~~~~~~~~~~方法~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     """
#
#     def study(self,course_name):
#         print(f'{self.name}正在学习{course_name}.')
#
#
# class Teacher(Person):
#     """教师"""
#
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self.title = title
#
#     def teach(self, course_name):
#         print(f'{self.name}{self.title}正在讲授{course_name}')
#
#
# stu1 = Student('白元芳', 21)
# stu2 = Student('狄仁杰', 22)
# tea1 = Teacher('武则天', 35, '副教授')
# stu1.eat()
# stu2.eat()
# tea1.eat()
# stu1.study('Python程序设计')
# tea1.teach('Python程序设计')
# stu2.study('数据科学导论')


# project67 - 扑克游戏(重制版)

# 类和类之间的关系可以粗略的分为 is-a关系（继承）、has-a关系（关联）和 use-a关系（依赖）。

# 很显然扑克和牌是 has-a 关系，因为一副扑克有（has-a）52 张牌；玩家和牌之间不仅有关联关系还有依赖关系，因为玩家手上有（has-a）牌而且玩家使用了（use-a）牌。

# from enum import Enum
# import random
#
#
# class Suite(Enum):
#     """花色(枚举)"""
#     SPADE, HEART, CLUB, DIAMOND = range(4)
#
#
# class Card:
#     """牌"""
#
#     def __init__(self, suite, face):
#         self.suite = suite
#         self.face = face
#
#     def __repr__(self):
#         suites = '♠♥♣♦'
#         faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#         return f'{suites[self.suite.value]}{faces[self.face]}'  # 返回牌的花色和点数
#
#     def __lt__(self, other):
#         if self.suite == other.suite:
#             return self.face < other.face
#         return self.suite.value < other.suite.value
#
#
# class Poker:
#     """扑克"""
#
#     def __init__(self):
#         self.cards = [Card(suite, face)
#                       for suite in Suite
#                       for face in range(1,14)]
#         self.current = 0    # 记录发牌位置的属性
#
#     def shuffle(self):
#         """洗牌"""
#         self.current = 0
#         random.shuffle(self.cards)      # 通过random模块的shuffle函数实现随机乱序
#
#     def deal(self):
#         """发牌"""
#         card = self.cards[self.current]
#         self.current += 1
#         return card
#
#     @property
#     def has_next(self):
#         """判断还有没有牌可以发"""
#         return self.current < len(self.cards)
#
#
# class Player:
#     """玩家"""
#
#     def __init__(self, name):
#         self.name = name
#         self.cards = []     # 玩家手里的牌
#
#     def get_one(self, card):
#         """摸牌"""
#         self.cards.append(card)
#
#     def arrange(self):
#         """整理手里的牌"""
#         self.cards.sort()
#
# # 测试
#
# for suite in Suite:
#     print(f'{suite}: {suite.value}')
#
# card1 = Card(Suite.SPADE, 5)
# card2 = Card(Suite.HEART, 13)
# print(card1)  # ♠5
# print(card2)  # ♥K
#
# poker = Poker()
# print(poker.cards)      # 洗牌前的牌
# poker.shuffle()
# print(poker.cards)      # 洗牌后的牌
#
# poker = Poker()
# poker.shuffle()
# players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
# # 将牌轮流发到每个玩家手上每人13张牌
# for _ in range(13):
#     for player in players:
#         player.get_one(poker.deal())
# # 玩家整理手里的牌输出名字和手牌
# for player in players:
#     player.arrange()
#     print(f'{player.name}:{player.cards}')


# project68 - 工资结算系统

# 要求：某公司有三种类型的员工，分别是部门经理、程序员和销售员。
# 需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。
# 其中，部门经理的月薪是固定 15000 元；
# 程序员按工作时间（以小时为单位）支付月薪，每小时 200 元；
# 销售员的月薪由 1800 元底薪加上销售额 5% 的提成两部分构成。

# from abc import ABCMeta, abstractmethod
#
#
# class Employee(metaclass=ABCMeta):
#     """员工"""
#
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod         # abstractmethod装饰器将其声明为抽象方法，所谓抽象方法就是只有声明没有实现的方法，声明这个方法是为了让子类去重写这个方法。
#     def get_salary(self):
#         """结算月薪"""
#         pass
#
#
# class Manager(Employee):
#     """部门经理"""
#
#     def get_salary(self):
#         return 15000.0
#
#
# class Programmer(Employee):
#     """程序员"""
#
#     def __init__(self, name, working_hour=0):
#         super().__init__(name)
#         self.working_hour = working_hour
#
#     def get_salary(self):
#         return 200 * self.working_hour
#
#
# class Saleman(Employee):
#     """销售员"""
#
#     def __init__(self, name, sales=0):
#         super().__init__(name)
#         self.sales = sales
#
#     def get_salary(self):
#         return 1800 + 0.05 * self.sales
#
#
# emps = [Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Programmer('荀彧'), Saleman('张辽')]
# for emp in emps:
#     if isinstance(emp,Programmer):          # isinstance函数来判断员工对象的类型
#         emp.working_hour = int(input(f'请输入{emp.name}本月的工作时间：'))
#     elif isinstance(emp,Saleman):
#         emp.sales = float(input(f'请输入{emp.name}本月销售额：'))
#     print(f'{emp.name}本月工资为：￥{emp.get_salary():.2f}元')