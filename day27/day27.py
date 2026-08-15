"""
day27

Author:ignorant-fool
Version:0.1
Date:2026/8/15
"""

# project117 - 用装饰器来实现单例模式

# from functools import wraps
#
# def singleton(cls):
#     """装饰类的装饰器"""
#     instances = {}
#
#     @wraps(cls)
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return wrapper
#
# @singleton
# class President:
#     """总统(单例类)"""
#
#     def __init__(self, name):
#         self.name = name
#
#     def sc(self):
#         print(self.name)
#
# a = President('奥巴马')
# b = President('美乐迪')
# a.sc()
# b.sc()


# project118 - 线程安全的单例装饰器

# from functools import wraps
# from threading import RLock
#
# def singleton(cls):
#     """线程安全的单例装饰器"""
#     instances = {}
#     locker = RLock()
#
#     @wraps(cls)
#     def wrapper(*args, **kwargs):
#         if cls not in instances:                                  # 外层 if 避免无意义抢锁提升性能。
#             with locker:
#                 if cls not in instances:                          # 内层 if 防止多个线程同时通过外层判断后，排队创建多个实例。
#                     instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return wrapper


# project119 - 工资结算系统

# 月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成

# from abc import ABCMeta, abstractmethod
#
# class Employee(metaclass=ABCMeta):
#     """员工(抽象类)"""
#
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def get_salary(self):
#         """结算月薪(抽象方法)"""
#         pass
#
# class Manager(Employee):
#     """部门经理"""
#
#     def get_salary(self):
#         return 15000.0
#
# class Programmer(Employee):
#     """程序员"""
#
#     def __init__(self, name, working_hour=0):
#         self.working_hour = working_hour
#         super().__init__(name)
#
#     def get_salary(self):
#         return 200.0 * self.working_hour
#
# class Salesman(Employee):
#     """销售员"""
#
#     def __init__(self, name, sales=0.0):
#         self.sales = sales
#         super().__init__(name)
#
#     def get_salary(self):
#         return 1800.0 + self.sales * 0.05
#
# class EmployeeFactory:
#     """创建员工的工厂(工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合)"""
#
#     def create(emp_type: str, *args, **kwargs):
#         all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
#         cls = all_emp_types[emp_type.upper()]
#         return cls(*args, **kwargs) if cls else None
#
# def main():
#     """主函数"""
#     emps = [
#         EmployeeFactory.create('M', '曹操'),
#         EmployeeFactory.create('P', '荀彧', 120),
#         EmployeeFactory.create('P', '郭嘉', 85),
#         EmployeeFactory.create('S', '典韦', 123000),
#     ]
#     for emp in emps:
#         print(f'{emp.name}:{emp.get_salary():.2f}')
#
# if __name__ == '__main__':
#     main()