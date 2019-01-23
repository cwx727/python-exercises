#including utf-8

#定义类
class Dog:
	#初始化默认的类的方法、属性
	def __init__(self,newweight,newcolor):
		self.weight = newweight
		self.color = newcolor
		
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

#创建一个小狗类
smallDog = Dog(5,"黄色")
#调用狗类的方法
smallDog.dark()
smallDog.run()

#添加小狗的属性
#smallDog.color = "黄色"
#smallDog.weight = 5

print(smallDog.color)
print(smallDog.weight)

smallDog.eat()
print('-----吃-----')	
print(smallDog.weight)

wangcai = Dog(10,"黑色")	
print('-----旺财-----')	
print(wangcai.color)
print(wangcai.weight)
