#encoding=utf-8

username = "python"
password = "a123456"

input_username = input("请输入用户名：")
input_password = input("请输入密码：")

if input_username==username and input_password==password:
	print("欢迎登录")
else:
	print("用户名或密码错误")

