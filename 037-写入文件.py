#include utf-8
filename1 = '/home/python/ftp/share/python练习题/bookfile/chapter_10/writefile1.txt'
filename2 = '/home/python/ftp/share/python练习题/bookfile/chapter_10/writefile2.txt'
filename3 = '/home/python/ftp/share/python练习题/bookfile/chapter_10/guest_book.txt'
filename4 = '/home/python/ftp/share/python练习题/bookfile/chapter_10/guest_reason.txt'


print("1.----------10.2.1 写入空文件------------")
with open(filename1, 'w') as file_object:
	file_object.write("I love programming.")
	
print("\n2.----------10.2.3 在文末添加------------")
with open(filename1, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
	
print("\n3.----------10-3 访客 ： 编写一个程序， 提示用户输入其名字； 用户作出响应后， 将其名字写入到文件guest.txt中。------------")
input_text = input('Please input:')

with open(filename2, 'w') as file_object:
	file_object.write(input_text)
	
print("\n4.----------10-4 访客名单 ： 编写一个while 循环， 提示用户输入其名字。 用户输入其名字后， 在屏幕上打印一句问候语， 并将一条访问记录添加到文件guest_book.txt中。 确保这个文件中的每条记录都独占一行。------------")
#input_text = input('Please input your name:')

while True:
	input_text = input('Please input your name:')
	if input_text != 'q!':
		with open(filename3, 'a') as file_object:
			file_object.write(input_text+'\n')
		print('welcome ' + input_text + '\nIf you want to quit, input key "q!"')
	else:
		break

print("\n5.----------10-5 关于编程的调查 ： 编写一个while 循环， 询问用户为何喜欢编程。 每当用户输入一个原因后， 都将其添加到一个存储所有原因的文件中。------------")

while True:
	print('welcome ' + input_text + '\nIf you want to quit, input key "q!"')
	input_text = input('Please input your reason:')
	if input_text != 'q!':
		with open(filename4, 'a') as file_object:
			file_object.write(input_text+'\n')
	else:
		break
