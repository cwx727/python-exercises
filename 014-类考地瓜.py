#including utf-8

class Sweetpotato:
	def __init__(self):
		self.cookLever = 0
		self.cookstring = '生的'
		self.cookcondiments = []
	
	def cook(self,time):
		self.cookLever += time
		if self.cookLever > 8:
			self.cookstring ='烤焦了'
		elif self.cookLever > 5:
			self.cookstring ='熟了'
		elif self.cookLever > 3:
			self.cookstring ='夹生的'
		else:
			self.cookstring ='生的'
		
digua = Sweetpotato()
print("----烤了2分钟----")
digua.cook(2)
print(digua.cookstring)
print("----又烤了2分钟----")
digua.cook(4)
print(digua.cookstring)


