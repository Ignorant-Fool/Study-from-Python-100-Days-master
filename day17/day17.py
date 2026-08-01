"""
day17

Author:ignorant-fool
Version:0.1
Date:2026/8/1
"""

# project81 - 读取Excel文件

# import datetime
# import openpyxl
#
# # 加载一个工作薄 ----> Workbook
# wb = openpyxl.load_workbook('阿里巴巴2020年股票数据.xlsx')
# # 获取工作表的名字
# print(wb.sheetnames)
# # 获取工作表
# sheet = wb.worksheets[0]
# # 获得单元格的范围
# print(sheet.dimensions)
# # 获得行数和列数
# print(sheet.max_row, sheet.max_column)
#
# # 获取指定单元格的值
# print(sheet.cell(3, 3).value)
# print(sheet['C3'].value)
# print(sheet['G255'].value)
#
# # 获取多个单元格(嵌套元组)
# print(sheet['A2:C5'])
#
# # 读取所有单元格的数据
# for row_ch in range(2, sheet.max_row + 1):
#     for col_ch in 'ABCDEFG':
#         value = sheet[f'{col_ch}{row_ch}'].value
#         if type(value) == datetime.datetime:
#             print(value.strftime('%Y年%m月%d日'), end='\t')
#         elif type(value) == int:
#             print(f'{value:<10d}', end='\t')
#         elif type(value) == float:
#             print(f'{value:.4f}', end='\t')
#         else:
#             print(value, end='\t')
#     print()


# project82 - 写Excel文件

# import random
# import openpyxl
#
# # 第一步：创建工作薄(Workbook)
# wb = openpyxl.Workbook()
#
# # 第二步：添加工作表(Worksheet)
# sheet = wb.active
# sheet.title = '期末成绩'
#
# # 第三步：添加数据
# titles = ['姓名', '语文', '数学', '英语']
# for col_index, title in enumerate(titles):
#     sheet.cell(1, col_index + 1, title)
#
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# for row_index, name in enumerate(names):
#     sheet.cell(row_index + 2, 1, name)
#     for col_index in range(2, 5):
#         sheet.cell(row_index + 2, col_index, random.randrange(50, 101))
#
# # 第四步：保存工作薄
# wb.save('考试成绩表.xlsx')


# project83 - 调整样式和公式计算

# import openpyxl
# from openpyxl.styles import Font, Alignment, Border, Side
#
# # 对齐方式
# align = Alignment(horizontal='center', vertical='center')
# # 边框线条
# side = Side(color='ff7f50', style='mediumDashed')
#
# wb = openpyxl.load_workbook('考试成绩表.xlsx')
# sheet = wb.worksheets[0]
#
# # 调整行高和列宽
# sheet.row_dimensions[1].height = 30
# sheet.column_dimensions['E'].width = 120
#
# sheet['E1'] = '平均分'
# # 设置字体
# sheet.cell(1, 5).font = Font(size=18, bold=True, color='ff1493', name='华文楷体')
# # 设置对齐方式
# sheet.cell(1, 5).alignment = align
# # 设置单元格边框
# sheet.cell(1, 5).border = Border(top=side, left=side, right=side, bottom=side)
# for i in range(2, 7):
#     # 公式计算每个学生的平均分
#     sheet[f'E{i}'] = f'=average(B{i}:D{i})'
#     sheet.cell(i, 5).font = Font(size=12, color='4169e1', italic=True)
#     sheet.cell(i, 5).alignment = align
#
# wb.save('考试成绩表.xlsx')


# project84 - 生成统计图表

# from openpyxl import Workbook
# from openpyxl.chart import BarChart, Reference
#
# wb = Workbook(write_only=True)
# sheet = wb.create_sheet()
#
# rows = [
#     ('类别', '销售A组', '销售B组'),
#     ('手机', 40, 30),
#     ('平板', 50, 60),
#     ('笔记本', 80, 70),
#     ('外围设备', 20, 10),
# ]
#
# # 向表单中添加行
# for row in rows:
#     sheet.append(row)
#
# # 创建图表对象
# chart = BarChart()
# chart.type = 'col'
# chart.style = 10
# # 设置图表的标题
# chart.title = '销售统计图'
# # 设置图表纵轴的标题
# chart.y_axis.title = '销量'
# # 设置图表横轴的标题
# chart.x_axis.title = '商品类别'
# # 设置数据的范围
# data = Reference(sheet,min_row=1, min_col=2, max_row=5, max_col=3)
# # 设置分类的范围
# cats = Reference(sheet, min_col=1, min_row=2, max_row=5)
# # 给图表添加数据
# chart.add_data(data, titles_from_data=True)
# # 给图表添加分类
# chart.set_categories(cats)
# chart.shape = 4
# # 将图表添加到表单指定的单元格中
# sheet.add_chart(chart,'A10')
# wb.save('demo.xlsx')


# project85 - 操作Word文档

# from docx import Document
# from docx.shared import Cm, Pt
# from docx.document import Document as Doc
#
# # 创建代表Word文档的Doc对象
# document = Document()
# # 添加大标题
# document.add_heading('快快乐乐学Python', 0)
# # 添加段落
# p = document.add_paragraph('Python是一门非常流行的语言，它')
# run = p.add_run('简单')
# run.bold = True
# run.font.size = Pt(18)
# p.add_run('而且')
# run = p.add_run('优雅')
# run.font.size =Pt(18)
# run.underline = True
# p.add_run('。')
# # 添加一级标题
# document.add_heading('Heading, level 1', level=1)
# # 添加带样式的段落
# document.add_paragraph('Intense quote',style='Intense Quote')
# # 添加无序列表
# document.add_paragraph('first item in unordered list',style='List Bullet')
# document.add_paragraph('second item in ordered list',style='List Bullet')
# # 添加有序列表
# document.add_paragraph('first item in ordered list', style='List Number')
# document.add_paragraph('second item in ordered list', style='List Number')
# # 添加图片（注意路径和图片必须要存在）
# document.add_picture('头像.jpg', width=Cm(5.2))
# # 添加分节符
# document.add_section()
# records = (
#     ('骆昊', '男', '1995-5-5'),
#     ('孙美丽', '女', '1992-2-2')
# )
# # 添加表格
# table = document.add_table(rows=1, cols=3)
# table.style = 'Dark List'
# hdr_cells = table.rows[0].cells
# hdr_cells[0].text = '姓名'
# hdr_cells[1].text = '性别'
# hdr_cells[2].text = '出生日期'
# # 为表格添加行
# for name, sex, birthday in records:
#     hdr_cells = table.add_row().cells
#     hdr_cells[0].text = name
#     hdr_cells[1].text = sex
#     hdr_cells[2].text = birthday
# # 添加分页符
# document.add_page_break()
# # 保存文档
# document.save('demo.docx')


# project86 - 获取docx文件内容

# from docx import Document
# from docx.document import Document as Doc
#
# doc = Document('demo.docx')  # type: Doc
# for no, p in enumerate(doc.paragraphs):
#     print(no, p.text)