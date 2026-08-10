"""
day22

Author:ignorant-fool
Version:0.1
Date:2026/8/10
"""

# project104 - 生成式(推导式)的用法

# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# # 用股票价格大于100元的股票狗砸一个新的字典
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)


# project105 - 嵌套的列表的坑

# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五名学生三门课程的成绩
# # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# # scores = [[None] * len(courses)] * len(names)
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩'))
#         print(scores)


# project106 - heapq模块(堆排序)

# 从列表中找出最大的或最小的N个元素
# 堆结构(大根堆/小根堆)

# import heapq
#
# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nlargest(2, list2, key=lambda x: x['price']))
# print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


# project107 - itertools模块

# 迭代工具模块

# import itertools
#
# # 产生ABCD的全排列
# print(list(itertools.permutations('ABCD')))
# # 产生ABCDE的五选三组合
# print(list(itertools.combinations('ABCDE', 3)))
# # 产生ABCD和123的笛卡尔积
# print(list(itertools.product('ABCD', '123')))
# # 产生ABC的无限循环序列
# it = itertools.cycle(('A', 'B', 'C'))
# for _ in range(6):
#     print(next(it), end=" ")


# project108 - collections模块

# from collections import Counter
#
# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
#     'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
#     'look', 'into', 'my', 'eyes', "you're", 'under'
# ]
# counter = Counter(words)
# print(counter)
# print(counter.most_common(3))


# project109 - 排序算法（选择、冒泡和归并）和查找算法（顺序和折半）

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]
    for i in range(len(items)):
        swapped = False
        for j in range(len(items) - i - 1):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items

def bubble_sort_plus(items, comp=lambda x, y: x > y):
    """搅拌排序(冒泡排序升级版)"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            for j in range(len(items) - i - 2, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j - 1], items[j] = items[j], items[j - 1]
                    swapped = True
        if not swapped:
            break
    return items

def merge(items1, items2, comp=lambda x, y: x < y):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

print(merge(list1, list2))