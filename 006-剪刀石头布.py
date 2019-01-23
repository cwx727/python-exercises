#including utf-8
import random

i=0

while i<5:
	player = int(input("请输入(0剪刀 1石头 2布):"))

	mac = random.randint(0,2)

	if (player ==0 and mac ==2) or (player ==1 and mac ==0) or (player ==0 and mac ==2):
		print("你赢了")
	elif (player == mac):
		print("平局")
	else:
		print("你输了")
		
	i+=1
