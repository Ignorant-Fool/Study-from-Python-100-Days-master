"""
day06

Author:ignorant-fool
Version:0.1
Date:2026/7/20
"""

# project34 - 集合类型的创建和遍历

# set1 = {1, 2, 3, 3, 3, 2}
# print(set1)
# set2 = {'Python', 'C++', 'Java', 'Swift', 'Python', 'Java'}
# print(set2)
# set3 = set('hello')
# print(set3)
# set4 = set([1, 2, 3, 3, 3, 2, 1])
# print(set4)
# set5 = {num for num in range(1,20) if num % 3 == 0 or num % 7 == 0}
# print(set5)
# set6 = {(1, 2, 3), (4, 5, 6)}
# print(set6)
# set7 = {[1, 2, 3], [4, 5, 6]}
# TypeError: unhashable type: 'list'
# set8 = {{1, 2, 3}, {4, 5, 6}}
# TypeError: unhashable type: 'set'

# for elem in set2:
#     print(elem)


# project35 - 集合的运算

# 成员运算
# set1 = {'Python', 'C++', 'Java', 'Swift', 'Kotlin'}
# set2 = {1, 2, 3, 4, 5, 6, 7}
# set3 = {2, 4, 6, 8, 10}
# print('Ruby' in set1)
# print('C++' not in set1)

# 交集
# print(set2 & set3)
# print(set2.intersection(set3))

# 并集
# print(set2 | set3)
# print(set2.union(set3))

# 差集
# print(set2 - set3)
# print(set2.difference(set3))
# print(set3 - set2)
# print(set3.difference(set2))

# 对称差
# print(set2 ^ set3)
# print(set2.symmetric_difference(set3))

# 子集
# print(set2 <= set3)
# print(set2.issubset(set3))
# print(set3 < set(range(1,11)))
# print(set2.issubset(set(range(1,11))))

# 超集
# print(set3 > {2, 6, 10})
# print(set3.issuperset({2, 6, 10}))

# 是否相交
# print({2, 4, 6}.isdisjoint({1, 3, 5}))
# print({2, 4, 6}.isdisjoint({2, 3, 5}))


# project36 - 集合对象的操作

# set1 = {1, 10, 100}

# 添加元素
# set1.add(1000)
# set1.add(10000)
# print(set1)

# 删除元素
# set1.discard(10)
# set1.remove(100)
# KeyError: 999
# set1.remove(999)
# print(set1)
# set1.pop()                                      # 随机删除一个元素
# print(set1)

# 清空元素
# set1.clear()
# print(set1)


# project37 - 定义字典类型的变量 - dict

# xinhua_dictionary = {
#     '麓': '山脚下',
#     '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
#     '蕗': '甘草的别名',
#     '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
# }
# print(xinhua_dictionary)

# person1 = {
#     'name': '王大锤',
#     'sex': True,
#     'birth': '1985-12-12',
#     'height': 168,
#     'weight': 65,
#     'addr': '成都市武侯区科华北路62号1栋101',
#     'tels': ['13122334455','13800998877'],
#     'friends': {'孙小美', '李元芳', '孙尚香'},
#     'cars': {
#         'brands': 'BMW',
#         'max_speed': '250',
#         'drive_type': '4WD'
#     }
# }
# print(person1)

# person2 = dict(name='孙小美',birth='1993-05-04',sex=False,tels=['13808092233'])
# print(person2)

# items1 = dict(zip('ABCDE',range(1,6)))
# print(items1)
# items2 = dict(zip('ABCDE',range(1,11)))
# print(items2)
# items3 = {x: x ** 3 for x in range(1,6)}
# print(items3)
# for key in person2:
#     print(key)
# for value in person2.values():                              # values函数可取出集合中的值
#     print(value)
# for key, value in person2.items():                          # items函数返回二元组：键值+自定义值
#     print(key,value)


# project38 - 字典的运算和操作

# person = dict(name='孙小美',birth='1993-05-04',sex=False)

# 成员运算
# print('name' in person)
# print('tels' in person)

# 索引运算
# print(person['name'])
# print(person['birth'])
# person['birth'] = '1995-10-08'
# person['address'] = '中国北京市海淀区西北旺东路18号院东区17'
# person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
# print(person)

# KeyError: 'tels'
# print(person['tels'])
# print(person.get('birth'))                              # get:当没有目标键值时，返回none，不会报错
# print(person.get('tels'))
# print(person.get('tels',['15912121313']))               # 可以设置默认值

# 删除元素
# print(person.pop('signature'))                         # 删除目标键值
# print(person)
# print(person.popitem())                                # popitem:删除末尾键值
# print(person)
# del person['sex']
# print(person)
# person.clear()
# print(person)


# project39 - 字典的应用-1

# 输入一段话，统计每个英文字母(忽略大小写)出现的次数，按出现次数从高到低输出。

# Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure.

# sentence = input('请输入：').lower()
# results = {}
# for ch in sentence:
#     if 'a' <= ch <= 'z':
#         results[ch] = results.get(ch,0) + 1
# print(results)
# sorted_keys = sorted(results, key=results.get, reverse=True)
# for key in sorted_keys:
#     print(f'{key}:{results[key]:>3d}次')


# project40 - 在一个字典中保存了股票的代码和价格

# 1.找出股价大于100元的股票并创建一个新的字典
# 2.按照股票价格从高到低输出股票代码和股票价格

# stocks = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }

# 1
# results = {}
# for key, value in stocks.items():
#     if value > 100:
#         results[key] = value
# print(results)

# 2:字典的生成式语法
# results = {key: value for key, value in stocks.items() if value > 100}
# print(results)

# sorted_keys = sorted(stocks, key=stocks.get, reverse= True)
# for key in sorted_keys:
#     print(f'{key:<5s}:{stocks[key]:8.2f}')