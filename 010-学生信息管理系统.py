#including utf-8

def showInfo():
	print("-"*20)
	print("  学生管理系统V1.0")
	print("1:添加")
	print("2:删除")
	print("3:修改")
	print("4:查询单个学生信息")
	print("5:查询所有学生信息")
	print("6:退出")
	print("-"*20)

allInfo=[]

def addInfo(name,stuId,age):
	stuInfo ={}
	stuInfo['name'] = name
	stuInfo['stuId'] = stuId
	stuInfo['age'] = age
	allInfo.append(stuInfo)
	return allInfo
	
def showOneinfo(stuId):
	for temp in allInfo:
		if temp['stuId'] == stuId:
			print("该学生信息是：%d      %s       %d"%(temp['stuId'],temp['name'],temp['age']))
		else:
			print("学生信息不存在")

def showAllinfo():
	for temp in allInfo:
		print("%d      %s       %d"%(temp['stuId'],temp['name'],temp['age']))
		
def modifyInfo(stuId):
	for temp in allInfo:
		if temp['stuId'] == stuId:
			print("学号   姓名   年龄")
			print("需要修改的学生信息是：%d      %s       %d"%(temp['stuId'],temp['name'],temp['age']))
			temp['name'] = input("请输入修改的姓名：")
			temp['stuId'] = int(input("请输入修改的学号："))
			temp['age'] = int(input("请输入修改的年龄："))
		else:
			print("学生信息不存在")
	return allInfo
		
def delinfo(stuId):
	for temp in allInfo:
		if temp['stuId'] == stuId:
			print("学号   姓名   年龄")
			print("需要删除的学生信息是：%d      %s       %d"%(temp['stuId'],temp['name'],temp['age']))
			conformInfo = input("请确认是否删除(Y：删除；N：不删除)")
			if conformInfo == 'Y':
				allInfo.remove(temp)
				print("学号为%d的信息删除成功"%stuId)
			else:
				continue
		else:
			print("学生信息不存在")
	return allInfo

while True:
	showInfo()
	key = int(input("请输入序号："))
	if key ==1:
		add_name = input("请输入姓名：")
		add_stuId = int(input("请输入学号："))
		add_age = int(input("请输入年龄："))
		addInfo(add_name,add_stuId,add_age)
	
	elif key == 2:
		stuId = int(input("请输入需要删除的学生学号："))
		delinfo(stuId)
	
	elif key == 3:
		stuId = int(input("请输入需要修改的学生学号："))
		modifyInfo(stuId)
				
	elif key == 4:
		stuId = int(input("请输入需要查询的学生学号："))
		showOneinfo(stuId)
		
	elif key == 5:
		print("学号   姓名   年龄")
		showAllinfo()
		
	elif key == 6:
		conformInfo_exit = input("请确认是否退出(Y：退出；N：不退出)")
		if conformInfo_exit == 'Y':
			break
	
	else:
		print("输入有误，请重新输入")
		
