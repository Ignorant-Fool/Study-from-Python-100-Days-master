"""
day15

Author:ignorant-fool
Version:0.1
Date:2026/7/30
"""

# project74 - 使用网络API获取数据

# import requests
#
# resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
# if resp.status_code == 200:
#     data_model = resp.json()
#     for news in data_model['newslist']:
#         print(news['title'])
#         print(news['url'])
#         print('-' * 60)


# project75 - 将数据写入CSV文件

# 现有五个学生三门课程的考试成绩需要保存到一个 CSV 文件中。
# 要达成这个目标，可以使用 Python 标准库中的csv模块，该模块的writer函数会返回一个csvwriter对象
# 通过该对象的writerow或writerows方法就可以将数据写入到 CSV 文件中。

# import csv
# import random
#
# with open('scores.csv','w',encoding='utf-8',newline='') as file:
#     writer = csv.writer(file,delimiter='|',quoting=csv.QUOTE_ALL)
#     writer.writerow(['姓名', '语文', '数学' , '英语'])
#     names = ['关羽' , '张飞', '赵云', '马超', '黄忠']
#     for name in names:
#         scores = [random.randrange(50,101) for _ in range(3)]
#         scores.insert(0, name)
#         writer.writerow(scores)


# project76 - 从CSV文件读取数据

# import csv
#
# with open('scores.csv','r',encoding='utf-8') as file:
#     reader = csv.reader(file,delimiter='|')
#     for data_list in reader:
#         print(reader.line_num,end='\t')
#         for elem in data_list:
#             print(elem,end='\t')
#         print()


# project77 - 读Excel文件

import xlrd

# 使用xlrd模块的open_workbook函数打开指定Excel文件并获得Book对象 (工作簿)
wb = xlrd.open_workbook('阿里巴巴2020年股票数据.xls')
# 通过Book对象的sheet_names方法可以获取所有表单名称
sheetnames = wb.sheet_names()
print(sheetnames)
# 通过指定的表单名称获取Sheet对象 (工作表)
sheet = wb.sheet_by_name(sheetnames[0])
# 通过Sheet对象的nrows和nclos属性获取表单的行数和列数
print(sheet.nrows, sheet.ncols)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        # 通过Sheet对象的cell方法获取指定Cell对象 (单元格)
        # 通过Cell对象的value属性获取单元格中的值
        value = sheet.cell(row, col).value
        # 对除首行外的其他行进行数据格式化处理
        if row > 0:
            # 第1列的xldate类型先转成元组再格式化为“年月日”的格式
            if col == 0:
                # xldate_as_tuple函数的第二个参数只有0和1两个取值
                # 其中0代表以1900-01-01为基准的日期，1代表以1904-01-01为基准的日期
                value = xlrd.xldate_as_tuple(value, 0)
                value = f'{value[0]}年{value[1]:>02d}月{value[2]:>02d}日'
            # 其他列的number类型处理成小数点后保留两位有效数字的浮点数
            else:
                value = f'{value:.2f}'
        print(value, end='\t')
    print()
# 获取最后一个单元格的数据类型
# 0 - 空值，1 - 字符串，2 - 数字，3 - 日期，4 - 布尔，5 - 错误
last_cell_type = sheet.cell_type(sheet.nrows - 1, sheet.ncols - 1)
print(last_cell_type)
# 获取第一行的值
print(sheet.row_values(0))
# 获取指定行指定列范围的数据（列表）
# 第一个参数代表行索引，第二个和第三个参数代表列的开始（含）和结束（不含）索引
print(sheet.row_slice(3, 0, 5))
