#including utf-8

class Animal(object):
	def __init__(self, name):
		self.__name = name
		
	def __del__(self):
		print('----删除对象的占用空间-----')

dog = Animal('xiaogou')
print('------1------')

'''
如果python解释器，检测到一个对象没有任何用处了，那就调用__del__kill掉对象
打印内容为
------1------
----删除对象的占用空间-----
'''			

		
		
	







