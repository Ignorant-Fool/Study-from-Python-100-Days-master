"""
day26

Author:ignorant-fool
Version:0.1
Date:2026/8/14
"""

# project115 - filter, map 以及它们的替代品

# items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
# items2 = [x ** 2 for x in range(1, 10) if x % 2]
#
# print(items1)
# print(items2)


# project116 - 装饰器函数

# from functools import wraps
# import time
#
# # #输出函数执行时间的装饰器
# # def record_time(func):
# #     """自定义装饰函数的装饰器"""
# #
# #     @wraps(func)
# #     def wrapper(*args, **kwargs):
# #         start = time.time()
# #         result = func(*args, **kwargs)
# #         print(f'{func.__name__}:{time.time() - start}')
# #         return result
# #
# #     return wrapper
#
# # 如果装饰器不希望跟print函数耦合，可以编写可以参数化的装饰器。
#
# ## 第一种
# # def record(output):
# #     """可以参数化的装饰器"""
# #
# #     def decorate(func):
# #
# #         @wraps(func)
# #         def wrapper(*args, **kwargs):
# #             start = time.time()
# #             result = func(*args, **kwargs)
# #             print(f'{func.__name__}:{time.time() - start}')
# #             return result
# #
# #         return wrapper
# #
# #     return decorate
#
# ## 第二种
# class Record():
#     """通过定义类的方法定义装饰器"""
#
#     def __init__(self, output):
#         self.output = output
#
#     def __call__(self, func):
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             result = func(*args, **kwargs)
#             print(f'{func.__name__}:{time.time() - start}')
#             return result
#
#         return wrapper
#
# # @record_time
# # @record("我是传入的参数")
# @Record('咕咕嘎嘎')
# def ceshi():
#     """测试装饰器"""
#
#     i = 13
#     while True:
#         time.sleep(1)
#         print(i)
#         i += 1
#         if i == 15:
#             break
#
# def main():
#     ceshi()
#     print(ceshi.__name__)
#     print(ceshi.__doc__)
#     ceshi.__wrapped__()
#
# if __name__ == '__main__':
#     main()