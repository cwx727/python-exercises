#include utf-8
filenames = ['not_exit_file.txt', 'alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
filedir = '/home/python/ftp/share/python练习题/bookfile/chapter_10/'


def count_words(file_dir_name,filename):
	try:
		with open(file_dir_name) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print( "Sorry, the file " + filename + " does not exist.")
	else:
		words = contents.split()
		print("The file " + filename + " has about " + str(len(words)) + " words.")

for filename in filenames:
	file_dir_name = filedir + filename
	count_words(file_dir_name,filename)
