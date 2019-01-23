#including utf-8

class Sweetpotato:
	def __init__(self):
		self.cookLever = 0
		self.cookstring = '生的'
		self.cookcondiments = []
		
	def __str__(self):
		msg = "地瓜处于" + self.cookstring + "的状态,"
		
		if len(self.cookcondiments) > 0:
			msg = msg + "添加的佐料为："
			for temp in self.cookcondiments:
				msg = msg + temp + ','
		msg = msg.strip(',')
		
		return msg
	
	def cook(self,time):
		self.cookLever += time
		if self.cookLever > 8:
			self.cookstring ='烤焦了'
		elif self.cookLever > 5:
			self.cookstring ='熟了'
		elif self.cookLever > 3:
			self.cookstring ='夹生的'
		else:
			self.cookstring ='生'
	
	def addcondiments(self,condiment):
		#添加佐料
		self.cookcondiments.append(condiment)
				
digua = Sweetpotato()
print("----烤了2分钟----")
digua.cook(2)
digua.addcondiments('番茄酱')
print(digua)
print("----又烤了4分钟----")
digua.cook(4)
digua.addcondiments('芥末酱')
print(digua)






