#include utf-8
import json

'''
10-11 喜欢的数字 ： 编写一个程序， 提示用户输入他喜欢的数字， 并使用json.dump() 将这个数字存储到文件中。 再编写一个程序， 从文件中读取这个值， 并打印
消息“I know your favorite number! It's _____.”。
'''

def read_favorite_num():
	filename = 'favorite_num.json'
	try:
		with open(filename) as j_obj:
			favorite_num = json.load(j_obj)
	except FileNotFoundError:
		return None
	else:
		return favorite_num
		
def write_favorite_num():
	favorite_num = input("Please input your favorite number:")
	filename = 'favorite_num.json'
	with open(filename, 'w') as j_obj:
		json.dump(favorite_num, j_obj)
	return favorite_num
	
def greet_num():
	favorite_num = read_favorite_num()
	if favorite_num:
		print("I know your favorite number! It's " + favorite_num)
	else:
		favorite_num = write_favorite_num()
		print("We'll remember your favorite number, " + favorite_num + "!")

greet_num()
