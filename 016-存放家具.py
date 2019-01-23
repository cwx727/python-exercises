#including utf-8

class Home:
	def __init__(self, area):
		self.area = area
		self.jiaju = []
		self.light = 'Off'
	
	def __str__(self):
		msg = "房子剩余可用面积为" + str(self.area)  
				
		if len(self.jiaju)>0:
			msg = msg + "\n当前房子中有的物品为：" 
			for temp in self.jiaju:
				msg = msg + temp.getBadName() + ','
				
			msg = msg.strip(' ,') 
		msg = msg + "\n房子当前的灯的状态为：" + self.light
		return msg
		
	def containItem(self, item):
		bedArea = item.getBadArea()
		bedName = item.getBadName()
		
		if self.area >= bedArea:
			self.jiaju.append(item)
			self.area -= bedArea
			print("当前添加%s成功，房子剩余可用面积为%d" %(bedName,self.area))
		else:
			print("房子剩余可用面积小于%s的面积，添加失败"%bedName)
			
	def turnOn(self):
		self.light = 'On'
		for temp in self.jiaju:
			temp.setLightOn()
			
	def turnOff(self):
		self.light = 'Off'
		for temp in self.jiaju:
			temp.setLightOff()
	
class Bed:
	def __init__(self, name, area):
		self.area =area
		self.name = name
		self.light = 'Off'
		
	def __str__(self):
		msg = self.name + "床占用的面积为" + str(self.area) + ';当前的明暗程度：' + self.light
		return msg
		
	def getBadArea(self):
		return self.area
	
	def getBadName(self):
		return self.name
		
	def setLightOn(self):
		self.light = 'On'
		
	def setLightOff(self):
		self.light = 'Off'
		
home = Home(180)
print(home)
print("-----席梦思------")
bed1 = Bed('席梦思',4)
home.containItem(bed1)
print(bed1)
print(home)
print("-----高低床------")
bed2 = Bed('高低床',10)	
home.containItem(bed2)
print(bed2)
print(home)
print("-----超级大床------")
bed3 = Bed('超级大床',170)
home.containItem(bed3)
print(bed3)
print(home)
print("-----开灯------")
home.turnOn()
print(home)
print(bed1)
print(bed2)
print(bed3)
print("-----关灯------")
home.turnOff()
print(home)
print(bed1)
print(bed2)
print(bed3)







