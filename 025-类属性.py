#including utf-8

class Animal(object):
	animalNum = 0
	def __init__(self,name,color):
		self.name = name
		self.color = color
		self.setAnimalNum()
		
	@classmethod
	def setAnimalNum(cls):
		cls.animalNum +=1
		
cat = Animal("猫","白色")
print(cat.animalNum)
dog = Animal("狗","黑色")
print(dog.animalNum)
	




		

		
		
	







