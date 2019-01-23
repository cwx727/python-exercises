#including utf-8

class Animal(object):
	def __init__(self, name, color):
		self.name = name    #用于继承的类，不能用私有属性，即self.__name
		self.color = color
		
	def __del__(self):
		print('----删除对象的占用空间-----')

#class Dog(父类名) 下面继承父类的所有方法，可在父类的基础上增加其他方法	
class Dog(Animal):
	def printInfo(self):
		print('狗的名字是：%s'%self.name)
		print('狗的颜色是：%s'%self.color)
		
xiaogou = Dog('小白', '白色')
xiaogou.printInfo()



		

		
		
	







