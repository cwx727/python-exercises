#including utf-8

class Test(object):
	def test1(self):
		print("啊啊啊。。。")

class Test_son(Test):
	def test1(self):     #对父类test1进行重写
		Test.test1(self)  #调用父类的方法
		super().test1()  #等同于Test.test1(self)
		
		print("喵喵")
	
		
test_son_o = Test_son()
test_son_o.test1()




		

		
		
	







