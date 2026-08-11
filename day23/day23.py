"""
day23

Author:ignorant-fool
Version:0.1
Date:2026/8/11
"""

# project110 - 穷举法 - 百人百鸡和五人分鱼

# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只

# for i in range(20):
#     for j in range(33):
#         z = 100 - i - j
#         if 5 * i + 3 * j + z // 3 == 100 and z % 3 == 0:
#             print(f'公鸡有{i}只，母鸡有{j}只，小鸡有{z}只。')
#
# # 参考答案
# for x in range(20):
#     for y in range(33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
#             print(x, y, z)

# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

# fish = 1
# while True:
#     a = fish
#     is_five = 0
#     for i in range(5):
#         if a % 5 == 1:
#             a = (a - 1) * 4 / 5
#             is_five += 1
#             if is_five == 5:
#                 break
#         else:
#             break
#     if is_five == 5:
#         print(f'有{fish}条鱼')
#         break
#     else:
#         fish += 1
#
# # 参考答案
# fish = 6
# while True:
#     total = fish
#     enough = True
#     for _ in range(5):
#         if (total - 1) % 5 == 0:
#             total = (total - 1) // 5 * 4
#         else:
#             enough = False
#             break
#     if enough:
#         print(fish)
#         break
#     fish += 5


# project111 - 贪婪法 - 在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。

# 假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。
#
# 名称	  价格（美元）	重量（kg）
# 电脑	  200	        20
# 收音机	  20	        4
# 钟	  175	        10
# 花瓶	  50	        2
# 书	  10	        1
# 油画	  90	        9
#
# 输入：
# 20 6
# 电脑 200 20
# 收音机 20 4
# 钟 175 10
# 花瓶 50 2
# 书 10 1
# 油画 90 9

# class Thing(object):
#     """物品"""
#
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     @property
#     def value(self):
#         """价格重量比"""
#         return self.price / self.weight
#
# def int_thing():
#     """输入物品信息"""
#     name, price, weight = input().split()
#     return name, int(price), int(weight)
#
# def main():
#     """主函数"""
#     max_weight, num_of_thing = map(int, input().split())
#     all_things = []
#     for _ in range(num_of_thing):
#         all_things.append(Thing(*int_thing()))
#     all_things.sort(key=lambda x: x.value, reverse=True)
#     total_weight = 0
#     total_price = 0
#     for thing in all_things:
#         if total_weight + thing.weight < max_weight:
#             print(f'小偷拿走了{thing.name}，价值{thing.price}美元，重{thing.weight}千克')
#             total_price += thing.price
#             total_weight += thing.weight
#     print(f'总价值：{total_price}美元，总质量{total_weight}千克')
#
# if __name__ == '__main__':
#     main()


# project112 - 分治法 - 快速排序

# 快速排序：选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大

# list0 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
#
# def quick_sort(items, comp=lambda x, y: x <= y):
#     items = list(items)[:]
#     _quick_sort(items, 0, len(items) - 1, comp)
#     return items
#
# def _quick_sort(items, start, end, comp):
#     if start < end:
#         pos = _partition(items, start, end, comp)
#         _quick_sort(items, start, pos - 1, comp)
#         _quick_sort(items, pos + 1, end, comp)
#
# def _partition(items, start, end, comp):
#     pivot = items[end]
#     i = start - 1
#     for j in range(start, end):
#         if comp(items[j], pivot):
#             i += 1
#             items[i], items[j] = items[j], items[i]
#     items[i + 1], items[end] = items[end], items[i + 1]
#     return i + 1
#
# print(quick_sort(list0))