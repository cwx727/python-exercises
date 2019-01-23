#including utf-8

class Animal(object):
	def bark(self):
		print("啊啊啊")
		
class Dog(Animal):
	def bark(self):
		print("汪汪汪")
		
class Cat(Animal):
	def bark(self):
		print("喵喵喵")

class Robot(object):
	def bark(self):
		print("嗡嗡嗡")
		
def animalBark(temp):
	temp.bark()
	
mao = Cat()
gou = Dog()
animalBark(mao)
animalBark(gou)
jiqiren = Robot()
animalBark(jiqiren)




		

		
		
	







