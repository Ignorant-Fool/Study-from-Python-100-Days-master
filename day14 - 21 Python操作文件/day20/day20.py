"""
day20

Author:ignorant-fool
Version:0.1
Date:2026/8/5
"""

# email_from = '发件人邮箱'
# email_to = '收件人邮箱'
# email_auth = '授权码'
# key = '螺丝帽的个人API-KEY'
# url = 'https://sms-api.luosimao.com/v1/send.json'
# phone = '收信人手机号'


# project96 - 发送电子邮件

# import smtplib
# from email.header import Header
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# # 创建邮件主体对象
# email = MIMEMultipart()
# # 设置发件人、收件人和主题
# email['From'] = email_from
# email['To'] = email_to
# email['Subject'] = Header('上半年工作情况汇报', 'utf-8')
# # 添加邮件正文内容
# content = """
# 据德国媒体报道，当地时间9日，德国火车司机工会成员进行了投票，
# 定于当地时间10日起进行全国性罢工，货运交通方面的罢工已于当地时间10日19时开始。
# 此后，从11日凌晨2时到13日凌晨2时，德国全国范围内的客运和铁路基础设施将进行48小时的罢工。"""
# email.attach(MIMEText(content, 'plain', 'utf-8'))
# # 创建SMTP_SSL对象（连接邮件服务器）
# smtp_obj = smtplib.SMTP_SSL('smtp.qq.com', 465)
# # 通过用户名和授权码进行登录
# smtp_obj.login(email_from, email_auth)
# # 发送邮件（发件人、收件人、邮件内容（字符串））
# smtp_obj.sendmail(
#     email_from,
#     email_to,
#     email.as_string()
# )


# # project97 - 发送带附件的邮件

# import smtplib
# from email.header import Header
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
# from urllib.parse import quote
#
# # 创建邮件主体对象
# email = MIMEMultipart()
# # 设置发件人、收件人和主题
# email['From'] = email_from
# email['To'] = email_to
# email['Subject'] = Header('请查收离职证明文件', 'utf-8')
# # 添加邮件正文内容（带HTML标签排版的内容）
# content = """<p>亲爱的前同事：</p>
# <p>你需要的离职证明在附件中，请查收！</p>
# <br>
# <p>祝，好！</p>
# <hr>
# <p>孙美丽 即日</p>"""
# email.attach(MIMEText(content, 'HTML', 'utf-8'))
# # 读取作为附件的文件
# with open('王大锤离职证明.docx', 'rb') as file:
#     attachment = MIMEApplication(file.read())
#     # 将中文文件名处理成百分号编码
#     filename = quote('王大锤离职证明.docx')
#     attachment.add_header(
#         "Content-Disposition",
#         "attachment",
#         filename=f"{filename}"
#     )
# email.attach(attachment)
#
# # 创建SMTP_SSL对象（连接邮件服务器）
# smtp_obj = smtplib.SMTP_SSL('smtp.qq.com', 465)
# # 通过用户名和授权码进行登录
# smtp_obj.login(email_from, email_auth)
# # 发送邮件（发件人、收件人、邮件内容（字符串））
# smtp_obj.sendmail(email_from,email_to,email.as_string())
# smtp_obj.quit()


# project98 - 将发送邮件封装成函数

# import smtplib
# from email.header import Header
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from urllib.parse import quote
#
# # 邮件服务器域名(自行修改)
# EMAIL_HOST = 'smtp.qq.com'
# # 邮件服务端口(通常是465)
# EMAIL_PORT = 465
# # 登录邮件服务器的账号(自行修改)
# EMAIL_USER = email_from
# # 开通SMTP服务的授权码（自行修改）
# EMAIL_AUTH = email_auth
#
#
# def send_email(*, from_user, to_users, subject='', content='', filenames=[]):
#     """发送邮件
#
#     :param from_user: 发件人
#     :param to_users: 收件人，多个收件人用英文分号进行分隔
#     :param subject: 邮件的主题
#     :param content: 邮件正文内容
#     :param filenames: 附件要发送的文件路径
#     """
#     email = MIMEMultipart()
#     email['From'] = from_user
#     email['To'] = to_users
#     email['Subject'] = Header(subject, 'utf-8').encode()
#
#     message = MIMEText(content, 'plain', 'utf-8')
#     email.attach(message)
#
#     # 替换前
#     # for filename in filenames:
#     #     with open(filename, 'rb') as file:
#     #         pos = filename.rfind('/')
#     #         display_filename = filename[pos + 1:] if pos >= 0 else filename
#     #         display_filename = quote(display_filename)
#     #         attachment = MIMEText(file.read(), 'base64', 'utf-8')
#     #         attachment['content-type'] = 'application/octet-stream'
#     #         attachment['content-disposition'] = f'attachment; filename="{display_filename}"'
#     #         email.attach(attachment)
#
#     # 替换后
#     from email.mime.application import MIMEApplication
#     for filename in filenames:
#         with open(filename, 'rb') as file:
#             pos = filename.rfind('/')
#             display_filename = filename[pos + 1:] if pos >= 0 else filename
#             attachment = MIMEApplication(file.read())
#             attachment.add_header('Content-Disposition', 'attachment', filename = display_filename)
#             email.attach(attachment)
#
#     smtp = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
#     smtp.login(EMAIL_USER, EMAIL_AUTH)
#     smtp.sendmail(from_user, to_users.split(';'), email.as_string())
#
# if __name__ == "__main__":
#     send_email(
#         from_user=EMAIL_USER,
#         to_users=email_to,
#         subject="请查收离职证明",
#         content="附件为离职证明文档",
#         filenames=["王大锤离职证明.docx"]
#     )


# project99 - 发送短信

# import random
#
# import requests
#
# def send_message(tel, message):
#     """发送短信(调用螺丝帽短信网关)"""
#     resp = requests.post(
#         url=url,
#         auth=('api', key),
#         data={
#             'mobile': tel,
#             'message': message
#         },
#         timeout = 10,
#         verify = False
#     )
#     return resp.json()
#
# def gen_mobile_code(length=6):
#     """生成指定长度的手机验证码"""
#     return ''.join(random.choices('0123456789', k=length))
#
# def main():
#     code = gen_mobile_code()
#     message = f'您的短信验证码是{code}，打死也不能告诉别人哟！！【铁壳测试】'
#     print(send_message(phone, message))
#
# if __name__ == '__main__':
#     main()