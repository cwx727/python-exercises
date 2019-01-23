#including utf-8

class Test(object):
	def test1(self):
		self.a = 100
		self.__b = 200
		print("-----父类：测试a、b能不能访问------")
		print(self.a)
		print(self.__b)
	
	#私有方法	
	def __test3(self):
		self.c = 100
		self.__d = 200
		print("-----父类：私有方法能不能访问------")
		print(self.a)
		print(self.__b)
	
	#通过父类中的另一个类访问私有方法（可以对类的方法进行封装）
	def test5(self):
		self.__test3()
		
#class Dog(父类名) 下面继承父类的所有方法，可在父类的基础上增加其他方法	
class Test_son(Test):
	def test2(self):
		print("-----子类：父类共有属性a能直接访问------")
		self.test1()
		print(self.a)
		print("-----子类：父类私有属性b不能直接访问------")
		#print(self.__b)#父类中的私有属性不能够继承
	
	def test4(self):
		print("-----子类：父类私有方法__test3不能直接访问------")
		#self.__test3()
		#print(self.d)
	
		
		
test_son_o = Test_son()
test_son_o.test2()
print("-----1------")
print("-----调用方法：通过子类继承的对象可以访问私有属性b能------")
test_son_o.test1()
test_son_o.test4()
print("-----2------")
print("-----调用方法：通过父类中的另一个类访问私有方法------")
test_son_o.test5()



		

		
		
	







