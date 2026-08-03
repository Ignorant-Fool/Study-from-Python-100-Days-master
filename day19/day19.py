"""
day19

Author:ignorant-fool
Version:0.1
Date:2026/8/3
"""

# project94 - 用Pillow处理图像

from PIL import Image

# # 读取图像获取image图像
# image = Image.open('头像.jpg')
# # 通过Image对象的format属性获得图像的格式
# print(image.format)     # JPEG
# # 通过Image对象的size属性
# print(image.size)       # (500,750)
# # 通过Image对象的mode属性获取对象的模式
# print(image.mode)       # RGB
# # 通过Image对象的show方法显示图像
# image.show()
# # 通过Image对象的crop方法指定剪裁区域剪裁图像
# image.crop((80, 20, 310, 360)).show()
# # 通过Image对象的thumbnail方法生成指定尺寸的缩略图
# image.thumbnail((128, 128))
# image.show()
# # 缩放和黏贴图像
# image1 = Image.open('头像.jpg')
# image2 = Image.open('头像.jpg')
# image1_crop = image1.crop((80, 20, 310, 360))
# width, height = image1_crop.size
# # 使用Image对象的resize方法修改图像的尺寸
# # 使用Image对象的paste方法粘贴
# image2.paste(image1_crop.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
# image2.show()