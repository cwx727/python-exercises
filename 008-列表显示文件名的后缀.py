#including utf-8

fileNames_list = ["001.py", "002.1.py", "00312322.txt", "004.rar"]

for fileName in fileNames_list:
	index = fileName.rfind(".")
	print(fileName[index:])
