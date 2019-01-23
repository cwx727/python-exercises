#include utf-8
filename1 = '/home/python/ftp/share/python练习题/bookfile/chapter_10/pi_digits.txt'
filename2 = '/home/python/ftp/share/python练习题/bookfile/chapter_10/pi_million_digits.txt'

print("1.----------10.1.1 读取整个文件------------")
# with 在不再需要访问文件后将其关闭。
with open(filename1) as file_object:  
	content = file_object.read()
	print(content)
	
print("\n2.----------10.1.3 逐行读取------------")	
with open(filename1) as file_object:
	for line in file_object:
		print(line.rstrip())   #rstrip去除后面行尾空格和换行符

print("\n3.----------10.1.4 创建一个包含文件各行内容的列表------------")		
with open(filename1) as file_object:
	lines = file_object.readlines()
	
for line in lines:
	print(line.rstrip())
	
print("\n4.----------10.1.5 内容并成一行------------")	
	
with open(filename1) as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip()
	
print(pi_string,len(pi_string))

print("\n5.----------10.1.6 包含一百万位的大型文件------------")	

with open(filename2) as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip()
	
print(pi_string[:52]+'...', len(pi_string))

print("\n6.----------10.1.7 圆周率值中包含你的生日吗------------")	
with open(filename2) as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip()
	
birthday = '1111'
if birthday in pi_string:
	print('Your birthday appears in the first million digits of pi!')
else:
	print('Your birthday does not appear in the first million digits of pi.')
