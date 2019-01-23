#including utf-8

#定义类
class Dog:
	#初始化默认的类的方法、属性
	def __init__(self,newname,newweight,newcolor):
		self.name = newname
		self.weight = newweight
		self.color = newcolor
	#魔法方法	
	def __str__(self):
		msg = "我的名字是" + self.name + "，体重是" + str(self.weight) + "，颜色是" + self.color
		return msg
		
	#定义类的方法
	def dark(self):
		print("汪汪汪")
	
	def run(self):
		print("跑...")
	
	def eat(self):
		#方法中定义属性
		print("吃...")
		#方法中对属性进行修改
		self.weight += 5
		
	def printname(self):
		print("小狗的名字是%s"%self.name)

#函数中调用类
def test(temp):
	temp.printname()
	temp.eat()

#创建一个小狗类
smallDog = Dog("小白",5,"黄色")
#小狗调用test函数
test(smallDog)
#魔法方法可以直接写对象名，直接调用__str__中的内容
print(smallDog)



