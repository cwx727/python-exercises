#include utf-8
import json

# 如果以前存储了用户名， 就加载它
# 否则， 就提示用户输入用户名并存储它

def get_stored_username():
	filename = 'username.json'

	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
		
def get_new_username(username):
    """Prompt for a new username."""
    #username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():

	#10-13 验证用户 ： 最后一个remember_me.py版本假设用户要么已输入其用户名， 要么是首次运行该程序。 我们应修改这个程序， 以应对这样的情形： 当前和最后一次运行该程序的用户并非同一个人。为此， 在greet_user() 中打印欢迎用户回来的消息前， 先询问他用户名是否是对的。 如果不对， 就调用get_new_username() 让用户输入正确的用户名。

    input_username = input("What is your name? ")
    username = get_stored_username()
    if input_username == username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username(input_username)
        print("We'll remember you when you come back, " + username + "!")

greet_user()	
