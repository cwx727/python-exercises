#including utf-8

#加object叫新式类，没有的是经典类
class Person(object):
	def __init__(self, name, age):
		#前面加__,是为了不让程序直接调用类的属性，如xiaoming.name,起到保护属性的作用
		self.__name = name
		self.__age = age
		
	def __str__(self):
		return "年龄为：" + str(self.__age)
	
	#需要访问或修改属性，需要通过方法
	def setNewAge(self,newage):
		if newage>0 and newage < 100:
			self.__age = newage
			
	def getAge(self):
		return self.__age
		
xiaoming = Person('xiaoming',18)
print(xiaoming)
print('---------------')
xiaoming.setNewAge(19)
print(xiaoming)
print('---------------')
ageTemp = xiaoming.getAge()
print(ageTemp)

		
		
	







