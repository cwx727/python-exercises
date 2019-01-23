#include utf-8
'''
10-10 加计算单词'the' 在每个文件中分别出现了多少次
'''
#include utf-8
filenames = ['not_exit_file.txt', 'alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
filedir = '/home/python/ftp/share/python练习题/bookfile/chapter_10/'

def count(file_dir_name,filename):
	try:
		with open(file_dir_name) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		print( "Sorry, the file " + filename + " does not exist.")
	else:
		content_count = contents.lower().count('the')
		print("The file " + filename + " has about " + str(content_count) + " word ‘the’.")

for filename in filenames:
	file_dir_name = filedir + filename
	count(file_dir_name,filename)
