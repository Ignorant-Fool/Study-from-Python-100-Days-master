"""
day16

Author:ignorant-fool
Version:0.1
Date:2026/7/31
"""

# project78 - 写Excel文件

#写入 Excel 文件可以通过xlwt 模块的Workbook类创建工作簿对象。
# 通过工作簿对象的add_sheet方法可以添加工作表。
# 通过工作表对象的write方法可以向指定单元格中写入数据。
# 最后通过工作簿对象的save方法将工作簿写入到指定的文件或内存中。

# import random
# import xlwt
#
# students_name = ['关羽', '张飞', '赵云', '马超', '黄忠']
# scores = [[random.randrange(50,101) for _ in range(3)] for _ in range(5)]
# # 创建工作薄对象(Workbook)
# wb = xlwt.Workbook()
# # 创建工作表对象(Worksheet)
# sheet = wb.add_sheet('一年级二班')
# # 添加表头数据
# titles = ('姓名', '语文', '数学', '英语')
# for index, title in enumerate(titles):
#     sheet.write(0, index, title)
# # 将学生姓名和考试成绩写入单元格
# for row in range(len(scores)):
#     sheet.write(row + 1, 0, students_name[row])
#     for col in range(len(scores[row])):
#         sheet.write(row + 1, col + 1, scores[row][col])
# # 保存Excel工作薄
# wb.save('考试成绩表.xls')


# project79 - 调整单元格格式

# 首先创建一个XFStyle对象，字体（Font）、对齐方式（Alignment）、边框（Border）和背景（Background）

# 如果希望将表头单元格的背景色修改为黄色
# header_style = xlwt.XFStyle()
# pattern = xlwt.Pattern()
# pattern.pattern = xlwt.Pattern.SOLID_PATTERN        # 给pattern对象的pattern属性赋值：开启实心填充模式。
# # 0 - 黑色、1 - 白色、2 - 红色、3 - 绿色、4 - 蓝色、5 - 黄色、6 - 粉色、7 - 青色
# pattern.pattern_fore_colour = 5
# header_style.pattern = pattern
# titles = ['姓名', '语文', '数学', '英语']
# for index, title in enumerate(titles):
#     sheet.write(0, index, title, header_style)

# 如果希望为表头设置指定的字体，可以使用Font类
# font = xlwt.Font()
# # 字体名称
# font.name = '华文楷体'
# # 字体大小(20是基准单位，18表示18px)
# font.height = 20 * 18
# # 是否使用粗体
# font.bold = True
# # 是否使用斜体
# font.isalic = False
# # 字体颜色
# font.colour_index = 1
# header_style.font = font

# 如果希望表头垂直居中对齐
# align = xlwt.Alignment()
# # 垂直方向的对齐方式
# align.vert = xlwt.Alignment.VERT_CENTER
# # 水平方向的对齐方式
# align.horz = xlwt.Alignment.HORZ_CENTER
# header_style.alignment = align

import xlwt
# 如果希望给表头加上红色的虚线边框
# borders = xlwt.Borders()
# props = (
#     ('top', 'top_color'), ('right', 'right_color'),
#     ('bottom', 'bottom_color'), ('left', 'left_color')
# )
# # 通过循环对四个方向的边框样式及颜色进行设定
# for position, color in props:
#     # 使用setattr内置函数动态给对象指定的属性赋值
#     setattr(borders, position, xlwt.Borders.DASHED)
#     setattr(borders, color, 2)
# header_style.borders = borders

# 如果要调整单元格的宽度（列宽）和表头的高度（行高）
# # 设置行高为40px
# sheet.row(0).set_style(xlwt.easyxf(f'font:height {20 * 40}'))
# titles = ('姓名', '语文', '数学', '英语')
# for index, title in enumerate(titles):
#     # 设置列宽为200px
#     sheet.col(index).width = 20 * 200
#     # 设置单元格的数据和样式
#     sheet.write(0, index, title,header_style)

# 最终结果
# import random
# import xlwt
#
# students_name = ('关羽', '张飞', '赵云', '马超', '黄忠')
# scores = [[random.randrange(50,101) for _ in range(3)] for _ in range(5)]
# # 创建工作薄对象(Workbook)
# wb = xlwt.Workbook()
# # 创建工作表对象(Worksheet)
# sheet = wb.add_sheet('一年级二班')
# # 添加表头数据
#
# header_style = xlwt.XFStyle()
# pattern = xlwt.Pattern()
# pattern.pattern = xlwt.Pattern.SOLID_PATTERN        # 给pattern对象的pattern属性赋值：开启实心填充模式。
# # 0 - 黑色、1 - 白色、2 - 红色、3 - 绿色、4 - 蓝色、5 - 黄色、6 - 粉色、7 - 青色
# pattern.pattern_fore_colour = 5
# header_style.pattern = pattern
#
# font = xlwt.Font()
# # 字体名称
# font.name = '华文楷体'
# # 字体大小(20是基准单位，18表示18px)
# font.height = 20 * 18
# # 是否使用粗体
# font.bold = True
# # 是否使用斜体
# font.isalic = False
# # 字体颜色
# font.colour_index = 2
# header_style.font = font
#
# align = xlwt.Alignment()
# # 垂直方向的对齐方式
# align.vert = xlwt.Alignment.VERT_TOP
# # 水平方向的对齐方式
# align.horz = xlwt.Alignment.HORZ_LEFT
# header_style.alignment = align
#
# borders = xlwt.Borders()
# props = (
#     ('top', 'top_color'), ('right', 'right_color'),
#     ('bottom', 'bottom_color'), ('left', 'left_color')
# )
# # 通过循环对四个方向的边框样式及颜色进行设定
# for position, color in props:
#     # 使用setattr内置函数动态给对象指定的属性赋值
#     setattr(borders, position, xlwt.Borders.DASHED)
#     setattr(borders, color, 2)
# header_style.borders = borders
#
# # 设置行高为40px
# sheet.row(0).set_style(xlwt.easyxf(f'font:height {20 * 40}'))
# titles = ('姓名', '语文', '数学', '英语')
# for index, title in enumerate(titles):
#     # 设置列宽为200px
#     sheet.col(index).width = 20 * 200
#     # 设置单元格的数据和样式
#     sheet.write(0, index, title,header_style)
#
# # 将学生姓名和考试成绩写入单元格
# for row in range(len(scores)):
#     sheet.write(row + 1, 0, students_name[row])
#     for col in range(len(scores[row])):
#         sheet.write(row + 1, col + 1, scores[row][col])
# # 保存Excel工作薄
# wb.save('考试成绩表.xls')


# project80 - 公式计算

# 统计全年收盘价（Close字段）的平均值以及全年交易量（Volume字段）的总和

# import xlrd
# import xlwt
# from xlutils.copy import copy
#
# wb_for_read = xlrd.open_workbook('阿里巴巴2020年股票数据.xls')
# sheet1 = wb_for_read.sheet_by_index(0)
# nrows, ncols = sheet1.nrows, sheet1.ncols
# wb_for_write = copy(wb_for_read)
# sheet2 = wb_for_write.get_sheet(0)
# sheet2.write(nrows, 4, xlwt.Formula(f'average(E2:E{nrows})'))
# sheet2.write(nrows, 6, xlwt.Formula(f'sum(G2:G{nrows})'))
# wb_for_write.save('阿里巴巴2020年股票数据.xls')