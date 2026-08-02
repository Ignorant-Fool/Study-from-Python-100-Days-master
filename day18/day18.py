"""
day18

Author:ignorant-fool
Version:0.1
Date:2026/8/2
"""

# project87 - 读取文件并替换信息

# from docx import Document
# from docx.document import Document as Doc
#
# # 将真实信息用字典的方式保存在列表中
# employees = [
#     {
#         'name': '骆昊',
#         'id': '100200198011280001',
#         'sdate': '2008年3月1日',
#         'edate': '2012年2月29日',
#         'department': '产品研发',
#         'position': '架构师',
#         'company': '成都华为技术有限公司'
#     },
#     {
#         'name': '王大锤',
#         'id': '510210199012125566',
#         'sdate': '2019年1月1日',
#         'edate': '2021年4月30日',
#         'department': '产品研发',
#         'position': 'Python开发工程师',
#         'company': '成都谷道科技有限公司'
#     },
#     {
#         'name': '李元芳',
#         'id': '2102101995103221599',
#         'sdate': '2020年5月10日',
#         'edate': '2021年3月5日',
#         'department': '产品研发',
#         'position': 'Java开发工程师',
#         'company': '同城企业管理集团有限公司'
#     },
# ]
# # 对列表进行循环遍历，批量生成Word文档
# for emp_dict in employees:
#     # 读取离职证明模板文件
#     doc = Document('离职证明模板.docx')
#     # 循环遍历所有段落寻找占位符
#     for p in doc.paragraphs:
#         if '{' not in p.text:
#             continue
#         # 不能直接修改段落内容，否则会丢失样式
#         # 所以需要对段落中的元素进行遍历并进行查找替换
#         for run in p.runs:
#             if '{' not in run.text:
#                 continue
#             # 将占位符换成实际内容
#             start, end = run.text.find('{'), run.text.find('}')
#             key, place_holder = run.text[start + 1: end], run.text[start: end + 1]
#             run.text = run.text.replace(place_holder, emp_dict[key])
#     # 每个人对应保存一个Word文档
#     doc.save(f'{emp_dict['name']}离职证明.docx')


# project88 - 生成PowerPoint

# from pptx import Presentation
#
# # 创建幻灯片对象
# pre = Presentation()
# # 选择母版添加一页
# title_slide_layout = pre.slide_layouts[0]
# slide = pre.slides.add_slide(title_slide_layout)
# # 获取标题栏和副标题栏
# title = slide.shapes.title
# subtitle = slide.placeholders[1]
# # 编辑标题和副标题
# title.text = 'Welcome to Python'
# subtitle.text = 'Life is short, I use Python'
# # 选择母版添加一页
# bullet_slide_layout = pre.slide_layouts[1]
# slide = pre.slides.add_slide(bullet_slide_layout)
# # 获取页面上所有形状
# shape = slide.shapes
# # 获取标题和主体
# title_shape = shape.title
# body_shape = shape.placeholders[1]
# # 编辑标题
# title_shape.text = 'Introduction'
# # 编辑主体内容
# tf = body_shape.text_frame
# tf.text = 'History of Python'
# # 添加一个一级段落
# p = tf.add_paragraph()
# p.text = 'X\'max 1989'
# p.level = 1
# # 添加一个二级段落
# p = tf.add_paragraph()
# p.text = 'Guido began to write interpreter for Python.'
# p.level = 2
# # 保存幻灯片
# pre.save('text.pptx')


# project89 - 从PDF中提取文本

# import PyPDF2
#
# reader = PyPDF2.PdfReader('test.pdf')
# for page in reader.pages:
#     print(page.extract_text())


# project90 - 旋转和叠加页面

# import PyPDF2
#
# reader = PyPDF2.PdfReader('test.pdf')
# writer = PyPDF2.PdfWriter()
#
# for no, page in enumerate(reader.pages):
#     if no % 2 == 0:
#         new_page = page.rotate(-90)
#     else:
#         new_page = page.rotate(90)
#     writer.add_page(new_page)
#
# with open('temp.pdf', 'wb') as file_obj:
#     writer.write(file_obj)


# project91 - 加密PDF文件

# import PyPDF2
#
# reader = PyPDF2.PdfReader('temp.pdf')
# writer = PyPDF2.PdfWriter()
#
# for page in reader.pages:
#     writer.add_page(page)
#
# writer.encrypt('foobared')
#
# with open('加密.pdf', 'wb') as file_obj:
#     writer.write(file_obj)


# project92 - 批量添加水印

# import PyPDF2
#
# reader1 = PyPDF2.PdfReader('temp.pdf')
# reader2 = PyPDF2.PdfReader('test.pdf')
# writer = PyPDF2.PdfWriter()
# watermaker_page = reader2.pages[0]
#
# for page in reader1.pages:
#     page.merge_page(watermaker_page)
#     writer.add_page(page)
#
# with open('水印.pdf', 'wb') as file_obj:
#     writer.write(file_obj)


# project93 - 创建PDF文件

# from reportlab.lib.pagesizes import A4
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfgen import canvas
#
# pdf_canvas = canvas.Canvas('test.pdf', pagesize=A4)
# width, height = A4
#
# # 绘图
# image = canvas.ImageReader('头像.jpg')
# pdf_canvas.drawImage(image, 20, height - 395, 250, 375)
#
# # 显示当前页
# pdf_canvas.showPage()
#
# # 注册字体文件
# pdfmetrics.registerFont(TTFont('Font1', 'ArialUnicode.ttf'))
# pdfmetrics.registerFont(TTFont('Font2', 'SimHei.ttf'))
#
# # 写字
# pdf_canvas.setFont('Font2', 40)
# pdf_canvas.setFillColorRGB(0.9, 0.5, 0.3, 1)
# pdf_canvas.drawString(width // 2 - 120, height // 2, '你好，世界！')
# pdf_canvas.setFont('Font1', 40)
# pdf_canvas.setFillColorRGB(0, 1, 0, 0.5)
# pdf_canvas.rotate(18)
# pdf_canvas.drawString(250, 250, 'hello, world!')
#
# # 保存
# pdf_canvas.save()