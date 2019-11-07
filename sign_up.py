"""
@brief  模仿用户登录
@Author  Ares
@Date    2019-10-23

"""

username = input("请输入用户名：")
password = input("请输入密码：")

if username == 'admin' and password == "123456":
    print("登录成功\r\n")
else:
    print("登录失败\r\n")